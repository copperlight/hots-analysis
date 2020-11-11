import json
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# JHow Per-Map Tier List & Build List - All Maps
JHOW_TIERLIST_SHEET_ID = '1IDYpfIfYxFKu4wvBbHJFtAlMjL_pHWEMcSWG3kGiT8A'

MAPS = [
    'Alterac Pass',
    'Battlefield',
    'Blackhearts',
    'Braxis Holdout',
    'Cursed Hollow',
    'Dragon Shire',
    'Garden of Terror',
    'Hanamura',
    'Infernal Shrines',
    'Sky Temple',
    'Tomb of the Spider',
    'Towers of Doom',
    'Volskaya',
    'Warhead Junction'
]

HERO_CLASSES = {
    'Healers': 'B19:K27',
    'Melee': 'M3:V15',
    'Ranged': 'B3:K15',
    'Tanks': 'M19:V27'
}


def get_credentials():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_sheet_resource():
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    return sheet


def get_values(sheet, map_name, sheet_range):
    result = sheet.values().get(
        spreadsheetId=JHOW_TIERLIST_SHEET_ID,
        range=f'{map_name}!{sheet_range}'
    ).execute()

    return result.get('values', [])


def build_histogram(histogram, values):
    tier_columns = [0, 2, 4, 6, 8]

    for row in values:
        for col, hero in enumerate(row):
            if col not in tier_columns or hero == '':
                continue
            tier = f'Tier {tier_columns.index(col) + 1}'
            if hero not in histogram:
                histogram[hero] = {tier: 1}
            elif tier not in histogram[hero]:
                histogram[hero][tier] = 1
            else:
                histogram[hero][tier] += 1


def hero_class_histogram(sheet, hero_class):
    histogram = {}

    for map_name in MAPS:
        print(f'build histogram for {hero_class} on map {map_name}')
        values = get_values(sheet, map_name, HERO_CLASSES[hero_class])
        build_histogram(histogram, values)

    return histogram


def build_tier_list(histogram):
    tier_list = {}

    for hero in histogram:
        rank = []

        for k, v in histogram[hero].items():
            rank.append((k, v))

        rank.sort(key=lambda x: x[1], reverse=True)

        tier, votes = rank[0][0], rank[0][1]

        if tier not in tier_list:
            tier_list[tier] = [f'{hero} ({votes})']
        else:
            tier_list[tier].append(f'{hero} ({votes})')

    tier_list = {k: tier_list[k] for k in sorted(tier_list)}

    for tier in tier_list:
        tier_list[tier].sort()

    return tier_list


def main():
    sheet = get_sheet_resource()

    for hero_class in HERO_CLASSES:
        histogram = hero_class_histogram(sheet, hero_class)
        tier_list = build_tier_list(histogram)

        with open(f'tier-list-{hero_class}.json', 'w') as f:
            f.write(json.dumps(tier_list, indent=4))


if __name__ == '__main__':
    main()
