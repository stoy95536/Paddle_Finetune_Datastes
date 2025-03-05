def lf_to_crlf(filename):
    """將檔案中的 LF 行尾符號轉換為 CRLF。"""
    try:
        with open(filename, 'r', newline='\n', encoding='utf-8') as f:
            content = f.read()

        with open(filename, 'w', newline='\r\n' , encoding='utf-8') as f:
            f.write(content)

        print(f"檔案 '{filename}' 的行尾符號已成功從 LF 轉換為 CRLF。")

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{filename}'。")
    except Exception as e:
        print(f"發生錯誤：{e}")

# 使用範例
lf_to_crlf('tra_dict_full.txt')