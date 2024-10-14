# About
Util for parsing items information from [Guns Girl - Houkai Gakuen 2](https://houkai2nd.miraheze.org/wiki/Houkai_Gakuen_2_Wiki)

# Preparations
1. Download `data_all` using [hg2-downloader](https://dev.s-ul.net/BLUEALiCE/hg2-downloader)
2. Extract `.txt` files from `data_all` using [AssetStudio](https://github.com/Perfare/AssetStudio)  
2.1. Since September 2023 there is an extractor in [hg2-downloader](https://dev.s-ul.net/BLUEALiCE/hg2-downloader), so u can use it instead
3. Files you need are `WeaponDataV3`, `CostumeDataV2`, `PassiveSkillDataV3`, `SpecialAttributeDataV2`, `PetData`, `PetSkillData`
4. Place these files in `hg2-item-parser/data/{server}` folder, where `{server}` is "JP" or "CN"
