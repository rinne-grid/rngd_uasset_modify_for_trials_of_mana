"""
0x0018-0x001B       : total_header_size
0x0029-0x002C       : name_count
0x002D-0x0030       : name_offset
0x0035-0x0038       : gatherable_text_data_offset
0x0039-0x003C       : export_count
0x003D-0x0040       : export_offset
0x0041-0x0044       : import_count
0x0045-0x0048       : import_offset
0x004D-0x0050       : string_asset_reference_count
0x0049-0x004C       : depends_offset
0x0051-0x0054       : string_asset_reference_offset
0x0055-0x0058       : searchable_names_offset
0x0059-0x005C       : thumbnail_table_offset
0x005D-0x0060       : guid a
0x0061-0x0064       : guid b
0x0065-0x0068       : guid c
0x0069-0x006C       : guid d
0x00A5-0x00A8       : asset_registry_data_offset
0x00A9-0x00AC       : build_data_start_offset
0x00BD-0x00C0       :

"""
import struct
import sys
from options import get_tools_options

ADDR_LIST = [
    # total_header_size
    (0x0018, 0x001B),
    # export_offset
    (0x003D, 0x0040),
    # import_offset
    (0x0045, 0x0048),
    # depends_offset
    (0x0049, 0x004C),
    # asset_registry_data_offset
    (0x00A5, 0x00A8),
    # build_data_start_offset
    (0x00A9, 0x00AC),
    (0x00BD, 0x00C0),
    # name_count
    # (0x0029, 0x002C)
]

EXPORT_COUNT_ADDR = 0x0039
EXPORT_OFFSET_ADDR = 0x003D
EXPORT_BYTE_SIZE = 104


def seek_and_get_bytes(fp, address, size_fmt):
    fp.seek(address)
    size = struct.calcsize(size_fmt)
    byte_size_pack = fp.read(size)
    byte_size_unpack = struct.unpack(size_fmt, byte_size_pack)[0]
    return byte_size_unpack


def seek_and_write_bytes(fp, address, size_fmt, value):
    fp.seek(address)
    packed_value = struct.pack(size_fmt, value)
    fp.write(packed_value)


def get_output_format(src_addr, dest_addr, addr_val_size, modify_val ):
    return f"{src_addr:#0x}-{dest_addr:#0x}:\t{addr_val_size:#10x}({addr_val_size:#10})\t->\t{modify_val:#10x}({modify_val:#10})"


def start_modify_uasset(filepath, size):
    add_size = size
    fmt_int_lte = "<i"
    print("Start modify bytes size...")
    with open(filepath, "r+b") as uasset:
        for addr in ADDR_LIST:
            addr_val_size = seek_and_get_bytes(uasset, addr[0], fmt_int_lte)
            modify_val = addr_val_size + add_size
            seek_and_write_bytes(uasset, addr[0], fmt_int_lte, modify_val)
            output = get_output_format(addr[0], addr[1], addr_val_size, modify_val)
            print(output)

        export_count_size = seek_and_get_bytes(uasset, EXPORT_COUNT_ADDR, fmt_int_lte)
        if export_count_size > 1:
            # export_sizeの合計はEXPORT_BYTE_SIZE
            print("Start modify export serial size...")
            current_address = seek_and_get_bytes(uasset, EXPORT_OFFSET_ADDR, fmt_int_lte)
            for i in range(export_count_size):
                # 36バイトseekし、serial_offsetの位置に移動する
                current_address = current_address + 36
                uasset.seek(current_address)
                export_start_addr = current_address
                export_offset_size = seek_and_get_bytes(uasset, current_address, fmt_int_lte)
                new_offset_size = export_offset_size + add_size
                seek_and_write_bytes(uasset, current_address, fmt_int_lte, new_offset_size)
                output = get_output_format(export_start_addr, export_start_addr+4, export_offset_size, new_offset_size)
                print(output)
                # 36バイトの位置にいるので、残り68バイトをseekで読み飛ばす
                current_address = current_address + 68
                uasset.seek(current_address)

    print("Complete!")


if __name__ == "__main__":
    args = sys.argv
    options = get_tools_options()
    print(options)
    start_modify_uasset(options.filepath, options.size)
