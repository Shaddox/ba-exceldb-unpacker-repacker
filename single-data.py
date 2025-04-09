import flatbuffers
from FlatData.CharacterDialogEventExcel import *


def test_deserialize():
    # The hex string from your database
    hex_string = "4000000000000000380078007000680060005800540050004C0000000000400000003C00000000003800340030002C002800240020001F0018001000080004003800000074000000859698000000000021030000000000000100000000000001780000007C000000B4000000F000000088010000E00100002002000024020000010000000000000000000000010000001A0000000300000021030000000000000A000000000000001E2700000000000025724D71000000001B000000435647726F75705F55494576656E744C6F6262795F456E7465723100010000000F9A03F5350000004D79206C6F72642120497427732074686520666573746976616C212057686572652073686F756C6420776520676F2066697273743F0000003A000000E698AFE685B6E585B8E594B7EFBC8CE4B8BBE585ACEFBC810AE4BE86EFBC8CE8A681E5BE9EE593AAE8A3A1E9968BE5A78BE78EA9E591A2EFBC9F000097000000E0B887E0B8B2E0B899E0B980E0B897E0B8A8E0B881E0B8B2E0B8A5E0B884E0B988E0B8B020E0B899E0B8B2E0B8A2E0B897E0B988E0B8B2E0B899210AE0B980E0B8A3E0B8B4E0B988E0B8A1E0B888E0B8B2E0B881E0B984E0B89BE0B980E0B897E0B8B5E0B988E0B8A2E0B8A7E0B897E0B8B5E0B988E0B984E0B8ABE0B899E0B881E0B988E0B8ADE0B899E0B894E0B8B5E0B884E0B8B03F0056000000E3818AE7A5ADE3828AE381A7E38199E38288E38081E4B8BBE6AEBFEFBC810AE38195E38182E38081E381A9E38193E3818BE38289E9818AE381B3E381AB0AE8A18CE3818DE381BEE38197E38287E38186E3818BEFBC9F00003C000000ECB695ECA09CEC9888EC9A942120ECA3BCEAB5B0210AEC9E902C20EC96B4EB9494EBB680ED84B020EB8680EB9FAC20EAB080EBB3BCEAB98CEC9A943F0000000002000000303700000000000000000000"

    # Convert hex to bytes
    blob_data = bytes.fromhex(hex_string)

    # Try to deserialize
    try:
        root = CharacterDialogEventExcel.GetRootAsCharacterDialogEventExcel(blob_data, 0)

        result = {
            # "CostumeUniqueId": root.CostumeUniqueId(),
            # "OriginalCharacterId": root.OriginalCharacterId(),
            # "DisplayOrder": root.DisplayOrder(),
            "EventID": root.EventID(),
            "ProductionStep_": root.ProductionStep(),
            "DialogCategory_": root.DialogCategory(),
            "DialogCondition_": root.DialogCondition(),
            "DialogConditionDetail_": root.DialogConditionDetail(),
            "DialogConditionDetailValue": root.DialogConditionDetailValue(),
            "GroupId": root.GroupId(),
            "DialogType_": root.DialogType(),
            "ActionName": root.ActionName().decode('utf-8') if root.ActionName() else None,
            "Duration": root.Duration(),
            "AnimationName": root.AnimationName().decode('utf-8') if root.AnimationName() else None,
            "LocalizeKR": root.LocalizeKR().decode('utf-8') if root.LocalizeKR() else None,
            "LocalizeJP": root.LocalizeJP().decode('utf-8') if root.LocalizeJP() else None,
            "LocalizeTH": root.LocalizeTH().decode('utf-8') if root.LocalizeTH() else None,
            "LocalizeTW": root.LocalizeTW().decode('utf-8') if root.LocalizeTW() else None,
            "LocalizeEN": root.LocalizeEN().decode('utf-8') if root.LocalizeEN() else None,
            # "LocalizeFR": root.LocalizeFR().decode('utf-8') if root.LocalizeFR() else None,

            # "LocalizeDE": root.LocalizeDE().decode('utf-8') if root.LocalizeDE() else None,
            # "VoiceId": [root.VoiceId(i) for i in range(root.VoiceIdLength())],
            # "CollectionVisible": root.CollectionVisible(),
            # "CVCollectionType_": root.CVCollectionType_(),
            # "UnlockEventSeason": root.UnlockEventSeason(),
            # "ScenarioGroupId": root.ScenarioGroupId(),
            # "LocalizeCVGroup": root.LocalizeCVGroup().decode('utf-8') if root.LocalizeCVGroup() else None
        }

        # Print result in a readable format
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Error deserializing: {str(e)}")
        # Print the first few bytes for debugging
        print(f"First few bytes: {blob_data[:16].hex()}")


def test_serialize():
    # Original hex string for comparison
    original_hex = "4000000000000000380078007000680060005800540050004C0000000000400000003C00000000003800340030002C002800240020001F0018001000080004003800000074000000859698000000000021030000000000000100000000000001780000007C000000B4000000F000000088010000E00100002002000024020000010000000000000000000000010000001A0000000300000021030000000000000A000000000000001E2700000000000025724D71000000001B000000435647726F75705F55494576656E744C6F6262795F456E7465723100010000000F9A03F5350000004D79206C6F72642120497427732074686520666573746976616C212057686572652073686F756C6420776520676F2066697273743F0000003A000000E698AFE685B6E585B8E594B7EFBC8CE4B8BBE585ACEFBC810AE4BE86EFBC8CE8A681E5BE9EE593AAE8A3A1E9968BE5A78BE78EA9E591A2EFBC9F000097000000E0B887E0B8B2E0B899E0B980E0B897E0B8A8E0B881E0B8B2E0B8A5E0B884E0B988E0B8B020E0B899E0B8B2E0B8A2E0B897E0B988E0B8B2E0B899210AE0B980E0B8A3E0B8B4E0B988E0B8A1E0B888E0B8B2E0B881E0B984E0B89BE0B980E0B897E0B8B5E0B988E0B8A2E0B8A7E0B897E0B8B5E0B988E0B984E0B8ABE0B899E0B881E0B988E0B8ADE0B899E0B894E0B8B5E0B884E0B8B03F0056000000E3818AE7A5ADE3828AE381A7E38199E38288E38081E4B8BBE6AEBFEFBC810AE38195E38182E38081E381A9E38193E3818BE38289E9818AE381B3E381AB0AE8A18CE3818DE381BEE38197E38287E38186E3818BEFBC9F00003C000000ECB695ECA09CEC9888EC9A942120ECA3BCEAB5B0210AEC9E902C20EC96B4EB9494EBB680ED84B020EB8680EB9FAC20EAB080EBB3BCEAB98CEC9A943F0000000002000000303700000000000000000000"

    # Create a FlatBuffer builder
    builder = flatbuffers.Builder(1024)

    # Create test data matching the structure from the schema
    data = {
        "CostumeUniqueId": 0,
        "OriginalCharacterId": 0,
        "DisplayOrder": 0,
        "EventID": 801,
        "ProductionStep": 3,
        "DialogCategory": 26,
        "DialogCondition": 1,
        "DialogConditionDetail": 0,
        "DialogConditionDetailValue": 0,
        "GroupId": 1,
        "DialogType": 0,
        "ActionName": None,
        "Duration": 0,
        "DurationKr": 0,
        "AnimationName": "07",
        "LocalizeKR": "축제예요! 주군!\n자, 어디부터 놀러 가볼까요?",
        "LocalizeJP": "お祭りですよ、主殿！\nさあ、どこから遊びに\n行きましょうか？",
        "LocalizeTH": "งานเทศกาลค่ะ นายท่าน!\nเริ่มจากไปเที่ยวที่ไหนก่อนดีคะ?",
        "LocalizeTW": "是慶典唷，主公！\n來，要從哪裡開始玩呢？",
        "LocalizeEN": "My lord! It's the festival! Where should we go first?"
    }

    # Create strings (in reverse order of how they'll be used)
    localize_cv_group = builder.CreateString("")
    localize_en = builder.CreateString(data["LocalizeEN"] if data["LocalizeEN"] else "")
    localize_tw = builder.CreateString(data["LocalizeTW"] if data["LocalizeTW"] else "")
    localize_th = builder.CreateString(data["LocalizeTH"] if data["LocalizeTH"] else "")
    localize_jp = builder.CreateString(data["LocalizeJP"] if data["LocalizeJP"] else "")
    localize_kr = builder.CreateString(data["LocalizeKR"] if data["LocalizeKR"] else "")
    animation_name = builder.CreateString(data["AnimationName"] if data["AnimationName"] else "")
    action_name = builder.CreateString(data["ActionName"] if data["ActionName"] else "")

    # Create VoiceId vector (empty for now)
    CharacterDialogEventExcelStartVoiceIdVector(builder, 0)
    voice_id_vector = builder.EndVector()

    # Start the CharacterDialogEventExcel
    CharacterDialogEventExcelStart(builder)

    # Add all fields in the correct order
    CharacterDialogEventExcelAddCostumeUniqueId(builder, data["CostumeUniqueId"])
    CharacterDialogEventExcelAddOriginalCharacterId(builder, data["OriginalCharacterId"])
    CharacterDialogEventExcelAddDisplayOrder(builder, data["DisplayOrder"])
    CharacterDialogEventExcelAddEventID(builder, data["EventID"])
    CharacterDialogEventExcelAddProductionStep(builder, data["ProductionStep"])
    CharacterDialogEventExcelAddDialogCategory(builder, data["DialogCategory"])
    CharacterDialogEventExcelAddDialogCondition(builder, data["DialogCondition"])
    CharacterDialogEventExcelAddDialogConditionDetail(builder, data["DialogConditionDetail"])
    CharacterDialogEventExcelAddDialogConditionDetailValue(builder, data["DialogConditionDetailValue"])
    CharacterDialogEventExcelAddGroupId(builder, data["GroupId"])
    CharacterDialogEventExcelAddDialogType(builder, data["DialogType"])
    CharacterDialogEventExcelAddActionName(builder, action_name)
    CharacterDialogEventExcelAddDuration(builder, data["Duration"])
    CharacterDialogEventExcelAddDurationKr(builder, data["DurationKr"])
    CharacterDialogEventExcelAddAnimationName(builder, animation_name)
    CharacterDialogEventExcelAddLocalizeKR(builder, localize_kr)
    CharacterDialogEventExcelAddLocalizeJP(builder, localize_jp)
    CharacterDialogEventExcelAddLocalizeTH(builder, localize_th)
    CharacterDialogEventExcelAddLocalizeTW(builder, localize_tw)
    CharacterDialogEventExcelAddLocalizeEN(builder, localize_en)
    CharacterDialogEventExcelAddVoiceId(builder, voice_id_vector)
    CharacterDialogEventExcelAddCollectionVisible(builder, False)
    CharacterDialogEventExcelAddCVCollectionType(builder, 0)
    CharacterDialogEventExcelAddUnlockEventSeason(builder, 0)
    CharacterDialogEventExcelAddScenarioGroupId(builder, 0)
    CharacterDialogEventExcelAddLocalizeCVGroup(builder, localize_cv_group)

    # Finish the buffer
    event = CharacterDialogEventExcelEnd(builder)
    builder.Finish(event)

    # Get the bytes
    buf = builder.Output()
    new_hex = buf.hex()

    # Print both hex strings for comparison
    print("Original hex:")
    print(original_hex)
    print("\nNew hex:")
    print(new_hex)

    # Print in 32-byte chunks for easier comparison
    print("\nSide by side comparison (32 bytes per line):")
    chunk_size = 32
    for i in range(0, max(len(original_hex), len(new_hex)), chunk_size):
        orig_chunk = original_hex[i:i + chunk_size]
        new_chunk = new_hex[i:i + chunk_size] if i < len(new_hex) else ""
        print(f"Original: {orig_chunk}")
        print(f"New:      {new_chunk}")
        print()

    return buf

if __name__ == "__main__":
    hex_string = "4000000000000000380078007000680060005800540050004C0000000000400000003C00000000003800340030002C002800240020001F0018001000080004003800000074000000859698000000000021030000000000000100000000000001780000007C000000B4000000F000000088010000E00100002002000024020000010000000000000000000000010000001A0000000300000021030000000000000A000000000000001E2700000000000025724D71000000001B000000435647726F75705F55494576656E744C6F6262795F456E7465723100010000000F9A03F5350000004D79206C6F72642120497427732074686520666573746976616C212057686572652073686F756C6420776520676F2066697273743F0000003A000000E698AFE685B6E585B8E594B7EFBC8CE4B8BBE585ACEFBC810AE4BE86EFBC8CE8A681E5BE9EE593AAE8A3A1E9968BE5A78BE78EA9E591A2EFBC9F000097000000E0B887E0B8B2E0B899E0B980E0B897E0B8A8E0B881E0B8B2E0B8A5E0B884E0B988E0B8B020E0B899E0B8B2E0B8A2E0B897E0B988E0B8B2E0B899210AE0B980E0B8A3E0B8B4E0B988E0B8A1E0B888E0B8B2E0B881E0B984E0B89BE0B980E0B897E0B8B5E0B988E0B8A2E0B8A7E0B897E0B8B5E0B988E0B984E0B8ABE0B899E0B881E0B988E0B8ADE0B899E0B894E0B8B5E0B884E0B8B03F0056000000E3818AE7A5ADE3828AE381A7E38199E38288E38081E4B8BBE6AEBFEFBC810AE38195E38182E38081E381A9E38193E3818BE38289E9818AE381B3E381AB0AE8A18CE3818DE381BEE38197E38287E38186E3818BEFBC9F00003C000000ECB695ECA09CEC9888EC9A942120ECA3BCEAB5B0210AEC9E902C20EC96B4EB9494EBB680ED84B020EB8680EB9FAC20EAB080EBB3BCEAB98CEC9A943F0000000002000000303700000000000000000000"
    test_deserialize()
    result = test_serialize()