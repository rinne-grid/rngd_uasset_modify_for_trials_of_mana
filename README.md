# Rngd Uasset Modify

## What is this?

This is a mod creation support tool for "Trials of Mana".   
If you change the number of bytes of uasset, such as adding to name, change the offset value that should be corrected in a batch.

## Install



## Usage

* launch cmd.exe or powershell.exe

* run exe
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


