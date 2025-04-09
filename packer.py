import sqlite3
import json
import os
import shutil
from flatbuffers import Builder
from FlatData.LocalizeSkillExcel import LocalizeSkillExcel
from FlatData.LocalizeExcel import LocalizeExcel
from FlatData.LocalizeEtcExcel import LocalizeEtcExcel
from FlatData.CharacterDialogFieldExcel import CharacterDialogFieldExcel
from FlatData.CharacterDialogEventExcel import CharacterDialogEventExcel
from FlatData.CharacterDialogExcel import CharacterDialogExcel
from FlatData.CharacterDialogSubtitleExcel import CharacterDialogSubtitleExcel
from FlatData.CharacterVoiceSubtitleExcel import CharacterVoiceSubtitleExcel
from FlatData.TutorialCharacterDialogExcel import TutorialCharacterDialogExcel


def ensure_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def create_localize_skill_blob(data):
    builder = Builder(1024)

    # Create strings
    name_kr = builder.CreateString(data["NameKr"] or "")
    desc_kr = builder.CreateString(data["DescriptionKr"] or "")
    skill_kr = builder.CreateString(data["SkillInvokeLocalizeKr"] or "")
    name_jp = builder.CreateString(data["NameJp"] or "")
    desc_jp = builder.CreateString(data["DescriptionJp"] or "")
    skill_jp = builder.CreateString(data["SkillInvokeLocalizeJp"] or "")
    name_th = builder.CreateString(data["NameTh"] or "")
    desc_th = builder.CreateString(data["DescriptionTh"] or "")
    skill_th = builder.CreateString(data["SkillInvokeLocalizeTh"] or "")
    name_tw = builder.CreateString(data["NameTw"] or "")
    desc_tw = builder.CreateString(data["DescriptionTw"] or "")
    skill_tw = builder.CreateString(data["SkillInvokeLocalizeTw"] or "")
    name_en = builder.CreateString(data["NameEn"] or "")
    desc_en = builder.CreateString(data["DescriptionEn"] or "")
    skill_en = builder.CreateString(data["SkillInvokeLocalizeEn"] or "")

    # Start building the FlatBuffer
    LocalizeSkillExcel.Start(builder)
    LocalizeSkillExcel.AddKey(builder, data["Key"])
    LocalizeSkillExcel.AddNameKr(builder, name_kr)
    LocalizeSkillExcel.AddDescriptionKr(builder, desc_kr)
    LocalizeSkillExcel.AddSkillInvokeLocalizeKr(builder, skill_kr)
    LocalizeSkillExcel.Add
    # ... Add all other fields ...

    localize = LocalizeSkillExcel.End(builder)
    builder.Finish(localize)
    return builder.Output()


# Similar functions for other types...

def update_table_data(cursor, table_name, json_data, blob_creator):
    for row in json_data:
        try:
            # Get the ID columns from the data
            id_cols = [row[f'col_{i}'] for i in range(len(row)) if f'col_{i}' in row]

            # Create WHERE clause based on ID columns
            where_clause = " AND ".join([f"col_{i}=?" for i in range(len(id_cols))])

            # Create the BLOB
            blob_data = blob_creator(row)

            # Update the database
            sql = f"UPDATE {table_name}DBSchema SET Bytes=? WHERE {where_clause}"
            cursor.execute(sql, [blob_data] + id_cols)

        except Exception as e:
            print(f"Error updating row in {table_name}: {e}")
            import traceback
            print(traceback.format_exc())


def main():
    # Create output directory and copy database
    ensure_directory('output')
    shutil.copy2('ExcelDB.db', 'output/ExcelDB.db')

    # Connect to the copied database
    conn = sqlite3.connect('output/ExcelDB.db')
    cursor = conn.cursor()

    # Process each table
    processors = {
        'LocalizeSkill': (create_localize_skill_blob, 'json/LocalizeSkill.json'),
        # Add other processors here...
    }

    for table_name, (processor, json_file) in processors.items():
        try:
            print(f"Processing {table_name}...")

            # Read JSON data
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Update database
            update_table_data(cursor, table_name, data, processor)

            print(f"Updated {len(data)} records in {table_name}")

        except Exception as e:
            print(f"Error processing table {table_name}: {e}")
            continue

    conn.commit()
    conn.close()
    print("Processing complete!")


if __name__ == "__main__":
    main()