import sqlite3
import json
import os
from FlatData.LocalizeSkillExcel import LocalizeSkillExcel
from FlatData.LocalizeExcel import LocalizeExcel
from FlatData.LocalizeEtcExcel import LocalizeEtcExcel
from FlatData.CharacterDialogFieldExcel import CharacterDialogFieldExcel
from FlatData.CharacterDialogEventExcel import CharacterDialogEventExcel
from FlatData.CharacterDialogExcel import CharacterDialogExcel
from FlatData.CharacterDialogSubtitleExcel import CharacterDialogSubtitleExcel
from FlatData.CharacterVoiceSubtitleExcel import CharacterVoiceSubtitleExcel
from FlatData.TutorialCharacterDialogExcel import TutorialCharacterDialogExcel


def decode_if_bytes(value):
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value


def process_localize_skill(blob_data):
    root = LocalizeSkillExcel.GetRootAsLocalizeSkillExcel(blob_data, 0)
    return {
        "Key": root.Key(),
        "NameKr": decode_if_bytes(root.NameKr()),
        "DescriptionKr": decode_if_bytes(root.DescriptionKr()),
        "SkillInvokeLocalizeKr": decode_if_bytes(root.SkillInvokeLocalizeKr()),
        "NameJp": decode_if_bytes(root.NameJp()),
        "DescriptionJp": decode_if_bytes(root.DescriptionJp()),
        "SkillInvokeLocalizeJp": decode_if_bytes(root.SkillInvokeLocalizeJp()),
        "NameTh": decode_if_bytes(root.NameTh()),
        "DescriptionTh": decode_if_bytes(root.DescriptionTh()),
        "SkillInvokeLocalizeTh": decode_if_bytes(root.SkillInvokeLocalizeTh()),
        "NameTw": decode_if_bytes(root.NameTw()),
        "DescriptionTw": decode_if_bytes(root.DescriptionTw()),
        "SkillInvokeLocalizeTw": decode_if_bytes(root.SkillInvokeLocalizeTw()),
        "NameEn": decode_if_bytes(root.NameEn()),
        "DescriptionEn": decode_if_bytes(root.DescriptionEn()),
        "SkillInvokeLocalizeEn": decode_if_bytes(root.SkillInvokeLocalizeEn())
    }


def process_localize(blob_data):
    root = LocalizeExcel.GetRootAsLocalizeExcel(blob_data, 0)
    return {
        "Key": root.Key(),
        "Kr": decode_if_bytes(root.Kr()),
        "Jp": decode_if_bytes(root.Jp()),
        "Th": decode_if_bytes(root.Th()),
        "Tw": decode_if_bytes(root.Tw()),
        "En": decode_if_bytes(root.En())
    }


def process_localize_etc(blob_data):
    root = LocalizeEtcExcel.GetRootAsLocalizeEtcExcel(blob_data, 0)
    return {
        "Key": root.Key(),
        "NameKr": decode_if_bytes(root.NameKr()),
        "DescriptionKr": decode_if_bytes(root.DescriptionKr()),
        "NameJp": decode_if_bytes(root.NameJp()),
        "DescriptionJp": decode_if_bytes(root.DescriptionJp()),
        "NameTh": decode_if_bytes(root.NameTh()),
        "DescriptionTh": decode_if_bytes(root.DescriptionTh()),
        "NameTw": decode_if_bytes(root.NameTw()),
        "DescriptionTw": decode_if_bytes(root.DescriptionTw()),
        "NameEn": decode_if_bytes(root.NameEn()),
        "DescriptionEn": decode_if_bytes(root.DescriptionEn())
    }


def process_character_dialog_field(blob_data):
    root = CharacterDialogFieldExcel.GetRootAsCharacterDialogFieldExcel(blob_data, 0)
    return {
        "GroupId": root.GroupId(),
        "MotionName": decode_if_bytes(root.MotionName()),
        "IsInteractionDialog": root.IsInteractionDialog(),
        "HideUI": root.HideUI(),
        "LocalizeKR": decode_if_bytes(root.LocalizeKR()),
        "LocalizeJP": decode_if_bytes(root.LocalizeJP()),
        "LocalizeTH": decode_if_bytes(root.LocalizeTH()),
        "LocalizeTW": decode_if_bytes(root.LocalizeTW()),
        "LocalizeEN": decode_if_bytes(root.LocalizeEN())
    }


def process_character_dialog_event(blob_data):
    root = CharacterDialogEventExcel.GetRootAsCharacterDialogEventExcel(blob_data, 0)
    return {
        "CostumeUniqueId": root.CostumeUniqueId(),
        "OriginalCharacterId": root.OriginalCharacterId(),
        "DisplayOrder": root.DisplayOrder(),
        "EventID": root.EventID(),
        "DialogConditionDetailValue": root.DialogConditionDetailValue(),
        "GroupId": root.GroupId(),
        "ActionName": decode_if_bytes(root.ActionName()),
        "Duration": root.Duration(),
        "DurationKr": root.DurationKr(),
        "AnimationName": decode_if_bytes(root.AnimationName()),
        "LocalizeKR": decode_if_bytes(root.LocalizeKR()),
        "LocalizeJP": decode_if_bytes(root.LocalizeJP()),
        "LocalizeTH": decode_if_bytes(root.LocalizeTH()),
        "LocalizeTW": decode_if_bytes(root.LocalizeTW()),
        "LocalizeEN": decode_if_bytes(root.LocalizeEN())
    }


def process_character_dialog(blob_data):
    root = CharacterDialogExcel.GetRootAsCharacterDialogExcel(blob_data, 0)
    return {
        "CharacterId": root.CharacterId(),
        "CostumeUniqueId": root.CostumeUniqueId(),
        "DisplayOrder": root.DisplayOrder(),
        "StartDate": decode_if_bytes(root.StartDate()),
        "EndDate": decode_if_bytes(root.EndDate()),
        "GroupId": root.GroupId(),
        "ActionName": decode_if_bytes(root.ActionName()),
        "Duration": root.Duration(),
        "DurationKr": root.DurationKr(),
        "AnimationName": decode_if_bytes(root.AnimationName()),
        "LocalizeKR": decode_if_bytes(root.LocalizeKR()),
        "LocalizeJP": decode_if_bytes(root.LocalizeJP()),
        "LocalizeTH": decode_if_bytes(root.LocalizeTH()),
        "LocalizeTW": decode_if_bytes(root.LocalizeTW()),
        "LocalizeEN": decode_if_bytes(root.LocalizeEN()),
        "ApplyPosition": root.ApplyPosition(),
        "PosX": root.PosX(),
        "PosY": root.PosY(),
        "UnlockFavorRank": root.UnlockFavorRank(),
        "UnlockEquipWeapon": root.UnlockEquipWeapon()
    }


def process_character_dialog_subtitle(blob_data):
    root = CharacterDialogSubtitleExcel.GetRootAsCharacterDialogSubtitleExcel(blob_data, 0)
    return {
        "LocalizeCVGroup": decode_if_bytes(root.LocalizeCVGroup()),
        "CharacterId": root.CharacterId(),
        "Duration": root.Duration(),
        "DurationKr": root.DurationKr(),
        "Separate": root.Separate(),
        "LocalizeKR": decode_if_bytes(root.LocalizeKR()),
        "LocalizeJP": decode_if_bytes(root.LocalizeJP()),
        "LocalizeTH": decode_if_bytes(root.LocalizeTH()),
        "LocalizeTW": decode_if_bytes(root.LocalizeTW()),
        "LocalizeEN": decode_if_bytes(root.LocalizeEN())
    }


def process_character_voice_subtitle(blob_data):
    root = CharacterVoiceSubtitleExcel.GetRootAsCharacterVoiceSubtitleExcel(blob_data, 0)
    return {
        "LocalizeCVGroup": decode_if_bytes(root.LocalizeCVGroup()),
        "CharacterVoiceGroupId": root.CharacterVoiceGroupId(),
        "Duration": root.Duration(),
        "DurationKr": root.DurationKr(),
        "Separate": root.Separate(),
        "LocalizeKR": decode_if_bytes(root.LocalizeKR()),
        "LocalizeJP": decode_if_bytes(root.LocalizeJP()),
        "LocalizeTW": decode_if_bytes(root.LocalizeTW()),
        "LocalizeTH": decode_if_bytes(root.LocalizeTH()),
        "LocalizeEN": decode_if_bytes(root.LocalizeEN())
    }


def process_tutorial_character_dialog(blob_data):
    root = TutorialCharacterDialogExcel.GetRootAsTutorialCharacterDialogExcel(blob_data, 0)
    return {
        "TalkId": root.TalkId(),
        "AnimationName": decode_if_bytes(root.AnimationName()),
        "LocalizeKR": decode_if_bytes(root.LocalizeKR()),
        "LocalizeJP": decode_if_bytes(root.LocalizeJP()),
        "LocalizeTH": decode_if_bytes(root.LocalizeTH()),
        "LocalizeTW": decode_if_bytes(root.LocalizeTW()),
        "LocalizeEN": decode_if_bytes(root.LocalizeEN()),
        "VoiceId": root.VoiceId()
    }


def extract_table_data(cursor, table_name, processor):
    cursor.execute(f"SELECT * FROM {table_name}DBSchema")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        if len(row) >= 2:
            try:
                blob_data = row[-1]  # Bytes column is always last
                processed_data = processor(blob_data)

                # Add the ID columns
                for i, col in enumerate(row[:-1]):
                    processed_data[f'col_{i}'] = col

                data.append(processed_data)

            except Exception as e:
                print(f"Error processing row in {table_name}: {e}")
                import traceback
                print(traceback.format_exc())

    return data


def main():
    # Create output directory
    if not os.path.exists('json'):
        os.makedirs('json')

    # Connect to the database
    conn = sqlite3.connect('ExcelDB.db')
    cursor = conn.cursor()

    # Process each table with its specific processor
    processors = {
        'LocalizeSkill': process_localize_skill,
        'Localize': process_localize,
        'LocalizeEtc': process_localize_etc,
        'CharacterDialogField': process_character_dialog_field,
        'CharacterDialogEvent': process_character_dialog_event,
        'CharacterDialog': process_character_dialog,
        'CharacterDialogSubtitle': process_character_dialog_subtitle,
        'CharacterVoiceSubtitle': process_character_voice_subtitle,
        'TutorialCharacterDialog': process_tutorial_character_dialog
    }

    for table_name, processor in processors.items():
        try:
            print(f"Processing {table_name}...")
            data = extract_table_data(cursor, table_name, processor)

            output_file = f'json/{table_name}.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"Saved {len(data)} records to {output_file}")

        except Exception as e:
            print(f"Error processing table {table_name}: {e}")
            continue

    conn.close()
    print("Processing complete!")


if __name__ == "__main__":
    main()