# Hitman-Hashes

## Statistics
| File Type | Total Resources | Correct Paths | Correct Percentage |
| --------- | --------------- | ------------- | ------------------ |
| AIBB      | 1               | 1             | 100.00%            |
| AIBX      | 1               | 1             | 100.00%            |
| AIBZ      | 5               | 4             | 80.00%             |
| AIRG      | 49              | 49            | 100.00%            |
| ALOC      | 26257           | 16518         | 62.91%             |
| ASEB      | 5816            | 1700          | 29.23%             |
| ASET      | 13487           | 6156          | 45.64%             |
| ASVA      | 277             | 267           | 96.39%             |
| ATMD      | 16911           | 6458          | 38.19%             |
| BMSK      | 59              | 38            | 64.41%             |
| BORG      | 6961            | 2620          | 37.64%             |
| BOXC      | 40              | 40            | 100.00%            |
| CBLU      | 2646            | 2646          | 100.00%            |
| CLNG      | 4               | 0             | 0.00%              |
| CPPT      | 2646            | 2646          | 100.00%            |
| CRMD      | 53              | 47            | 88.68%             |
| DITL      | 4               | 0             | 0.00%              |
| DLGE      | 48478           | 45853         | 94.59%             |
| DSWB      | 5               | 0             | 0.00%              |
| ECPB      | 2834            | 0             | 0.00%              |
| ECPT      | 2834            | 0             | 0.00%              |
| ENUM      | 2               | 1             | 50.00%             |
| ERES      | 270             | 266           | 98.52%             |
| FXAC      | 4               | 4             | 100.00%            |
| FXAS      | 349768          | 349059        | 99.80%             |
| GFXF      | 41              | 41            | 100.00%            |
| GFXI      | 11752           | 9122          | 77.62%             |
| GFXV      | 317             | 119           | 37.54%             |
| GIDX      | 1               | 1             | 100.00%            |
| HIKC      | 2               | 2             | 100.00%            |
| JSON      | 3117            | 1466          | 47.03%             |
| LINE      | 32101           | 25337         | 78.93%             |
| LOCM      | 16              | 14            | 87.50%             |
| LOCR      | 9627            | 5389          | 55.98%             |
| MATB      | 5439            | 4791          | 88.09%             |
| MATE      | 1102            | 829           | 75.23%             |
| MATI      | 18655           | 17373         | 93.13%             |
| MATT      | 5438            | 4790          | 88.08%             |
| MJBA      | 19585           | 7363          | 37.60%             |
| MRTN      | 2248            | 1073          | 47.73%             |
| MRTR      | 853             | 85            | 9.96%              |
| NAVP      | 77              | 75            | 97.40%             |
| ORES      | 9               | 7             | 77.78%             |
| PREL      | 141             | 141           | 100.00%            |
| PRIM      | 42720           | 21841         | 51.13%             |
| REPO      | 2               | 2             | 100.00%            |
| RTLV      | 141             | 0             | 0.00%              |
| SCDA      | 877             | 818           | 93.27%             |
| SDEF      | 500             | 500           | 100.00%            |
| TBLU      | 55852           | 39195         | 70.18%             |
| TELI      | 65278           | 34674         | 53.12%             |
| TEMP      | 85402           | 58193         | 68.14%             |
| TEXD      | 43309           | 32226         | 74.41%             |
| TEXT      | 44088           | 32570         | 73.87%             |
| UICB      | 393             | 393           | 100.00%            |
| UICT      | 393             | 393           | 100.00%            |
| VIDB      | 94              | 0             | 0.00%              |
| VTXD      | 11307           | 8695          | 76.90%             |
| WBNK      | 844             | 814           | 96.45%             |
| WMDA      | 9               | 9             | 100.00%            |
| WSGB      | 142             | 131           | 92.25%             |
| WSGT      | 142             | 131           | 92.25%             |
| WSWB      | 61              | 46            | 75.41%             |
| WSWT      | 66              | 46            | 69.70%             |
| WWEM      | 381505          | 121476        | 31.84%             |
| WWES      | 185757          | 185757        | 100.00%            |
| WWEV      | 26071           | 18867         | 72.37%             |
| WWFX      | 17082           | 16189         | 94.77%             |
| YSHP      | 4               | 3             | 75.00%             |

## Game flags
| Game    | Bit Representation (Binary) |
| ------- | --------------------------- |
| inAlpha | 0b000001                    |
| inH1    | 0b000010                    |
| inH2    | 0b000100                    |
| inH3    | 0b001000                    |
| inBeta  | 0b010000                    |
| inSA    | 0b100000                    |

## Scripts
This repository contains three main scripts merge.py and add_paths.py, add_new_hashes.py. They must be ran from the repository's root directory like `python ./scripts/add_paths.py`.

### merge.py
Generates the hash_list.txt. Takes a version number as an argument.

### add_paths.py
Adds paths to their assoicated hashes within the path's JSON files.

Requires a `new_paths.txt` file in the repository's root directory which contains data structured like:

```
000A4FB9B5FDAB19.WSGT,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/fashionshowmusic_level_state.wwisestategroup].pc_entitytype
004B66043E12A8E3.WSGB,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/fashionshowmusic_level_state.wwisestategroup].pc_entityblueprint
005EA1E72FC62DEC.WSGT,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/paris_rain_puddle_state.wwisestategroup].pc_entitytype
0054C5081030A3D0.WSGB,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/paris_rain_puddle_state.wwisestategroup].pc_entityblueprint
```

### add_new_hashes.py
Adds new hashes into the JSON files.

Requires a `new_hashes.txt` file in the repository's root directory which contains data structured like:

```
000A4FB9B5FDAB19.WSGT:h3
004B66043E12A8E3.WSGB:h3
005EA1E72FC62DEC.WSGT:h3
0054C5081030A3D0.WSGB:h3
003B993A25498AE6.AIBB:h2,h3
```

Possible games are: `alpha`, `h1`, `h2`, `h3`, `beta` and `sa`.