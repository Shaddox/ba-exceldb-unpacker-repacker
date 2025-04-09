import sqlite3
import flatbuffers
import json
from pathlib import Path
import importlib
import sys
from FlatData.TutorialCharacterDialogExcel import TutorialCharacterDialogExcel
import flatbuffers

def test_single_blob():
    """Test deserialization of a single BLOB"""
    conn = sqlite3.connect('ExcelDB.db')
    cursor = conn.cursor()

    try:
        # Get a single row
        cursor.execute('SELECT * FROM TutorialCharacterDialogDBSchema LIMIT 1')
        row = cursor.fetchone()

        if not row:
            print("No data found in table")
            return

        # Get the Bytes column
        cursor.execute('PRAGMA table_info(TutorialCharacterDialogDBSchema)')
        columns = cursor.fetchall()
        bytes_index = next(i for i, col in enumerate(columns) if col[1] == 'Bytes')

        blob_data = row[bytes_index]

        # Print some debug info
        print(f"\nBlob size: {len(blob_data)} bytes")
        print(f"First 16 bytes: {blob_data[:16].hex()}")

        # Try direct instantiation
        try:
            print("\nTrying direct method access...")
            root = TutorialCharacterDialogExcel.GetRootAsTutorialCharacterDialogExcel(blob_data, 0)
            print("Direct method access successful!")

            # Try to access some fields
            print("\nTrying to access fields:")
            print(f"TalkId: {root.TalkId()}")
            print(f"LocalizeKR: {root.LocalizeKR().decode('utf-8') if root.LocalizeKR() else None}")
            print(f"LocalizeJP: {root.LocalizeJP().decode('utf-8') if root.LocalizeJP() else None}")

        except Exception as e:
            print(f"Error during direct access: {str(e)}")
            print(f"Error type: {type(e)}")
            import traceback
            traceback.print_exc()

        # Try through reflection
        try:
            print("\nTrying through reflection...")
            method = getattr(TutorialCharacterDialogExcel, 'GetRootAsTutorialCharacterDialogExcel')
            print(f"Method type: {type(method)}")
            print(f"Method dir: {dir(method)}")

            root = method(blob_data, 0)
            print("Reflection access successful!")
            print("Flatbuffers version: " + flatbuffers.__version__)


        except Exception as e:
            print(f"Error during reflection: {str(e)}")
            print(f"Error type: {type(e)}")
            import traceback
            traceback.print_exc()

    finally:
        conn.close()


if __name__ == "__main__":
    test_single_blob()