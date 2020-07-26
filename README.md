# Rngd Uasset Modify

## What is this?

This is a mod creation support tool for "Trials of Mana".   
If you change the number of bytes of uasset, such as adding to name, change the offset value that should be corrected in a batch.

## Install

* Download the tool from the [Releases page](https://github.com/rinne-grid/rngd_uasset_modify_for_trials_of_mana/releases).
* Find the rngd_uasset_modify_for_trials_of_mana_vx.x.x.zip.
* Unzip the zip file

## Usage

* launch cmd.exe or powershell.exe

* Run um.exe as below
```shell script
um.exe uasset_file_path byte_size
```

### examples

* To increase the value of each offset in the ShopItemDataCsv.uasset file by 96 bytes

```shell script
um.exe "C:\tom_work\ShopItemDataCsv.uasset" 96
```

* To decrease the value of each offset in the ItemDataBase.uasset file by 50 bytes

```shell script
um.exe "C:\tom_work\ItemDataBase.uasset" -50
```


## development

* Python3.7

```python
pip install pipenv
python main.py path size
```

## Tips

This tool changes the following byte addresses.

|address|contents|
|-------|--------|
|0x0018-0x001B|total_header_size|
|0x003D-0x0040|export_offset|
|0x0045-0x0048|import_offset|
|0x0049-0x004C|depends_offset|
|0x00A5-0x00A8|asset_registry_data_offset|
|0x00A9-0x00AC|build_data_start_offset|
|0x00BD-0x00C0|preload_dependency_offset|

In addition, change the serial_size of each export based on the export_size.

[japanese]

## これは何?

これは、「Trials of Mana」のmod作成支援ツールです。  
nameへの追加など、uassetのバイト数を変更した場合に、修正すべきオフセット値を一括で変更します。

## インストール

*  [リリースページ](https://github.com/rinne-grid/rngd_uasset_modify_for_trials_of_mana/releases) からrngd_uasset_modify_for_trials_of_mana_vx.x.x.zipを見つけてダウンロードします。
* ダウンロードしたzipファイルを展開します

## 使い方

* cmd.exeかPowerShellを起動します

* 以下のように、um.exeを実行します
```shell script
um.exe uasset_file_path byte_size
```

### 例

* ShopItemDataCsv.uassetファイルのオフセットバイト数を96バイト増やしたい場合

```shell script
um.exe "C:\tom_work\ShopItemDataCsv.uasset" 96
```

* ItemDataBase.uassetファイルのオフセットバイト数を50バイト減らしたい場合

```shell script
um.exe "C:\tom_work\ItemDataBase.uasset" -50
```


## 開発について

* Python3.7

```python
pip install pipenv
python main.py path size
```

## Tips

このツールは以下のアドレスの値を変更します。

|address|contents|
|-------|--------|
|0x0018-0x001B|total_header_size|
|0x003D-0x0040|export_offset|
|0x0045-0x0048|import_offset|
|0x0049-0x004C|depends_offset|
|0x00A5-0x00A8|asset_registry_data_offset|
|0x00A9-0x00AC|build_data_start_offset|
|0x00BD-0x00C0|preload_dependency_offset|

上記に加えて、export_sizeを元に各exportのserial_sizeを変更します
