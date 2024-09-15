#!/usr/bin/env python
#%%
import os 
import sys
import pathlib
import shutil

import random
num_files = 10000
#%%
args = sys.argv
vault_path = "./test_vault"

# if len(args)>1:
#     num_files = int(args[1])
# if pathlib.Path(vault_path).is_dir():
#     shutil.rmtree(vault_path)
#     # os.removedirs(vault_path)

# os.mkdir(vault_path)
# %%
list_of_all_files = list(range(0, num_files))
list_of_all_files = [f"[[file_{num}{"".join(random.sample(["🤣","😂","😊","😱","😔","😆","🤬","✅"],k=2))}.md]]" for num in list_of_all_files]

for file_name in range(0,num_files):
    with open(f"{vault_path}/file_{file_name}.md", "w", encoding="utf-8") as file:
        sampled_notes = random.sample(list_of_all_files,k=10)
        links_text = " ".join(sampled_notes)
        file.write(f"""
[[file_1.md]]
```dataview
table time-played, length, rating
from "games"
sort rating desc
```
{links_text}
```\n--\n    -\\-                                                     \n    \\-- \\-                                                  \n     \\  - -\\                                                \n      \\      \\\\                                             \n       \\       \\                                            \n        \\       \\\\                                              \n         \\        \\\\                                            \n         \\          \\\\                                        \n         \\           \\\\\\                                      \n          \\            \\\\                                                 \n           \\            \\\\                                              \n           \\. .          \\\\                                  \n            \\    .       \\\\                                 \n             \\      .    \\\\                                            \n              \\       .  \\\\                                 \n              \\         . \\\\                                           \n              \\            <=)                                         \n              \\            <==)                                         \n              \\            <=)                                           \n               \\           .\\\\                                           _-\n               \\         .   \\\\                                        _-//\n               \\       .     \\\\                                     _-_/ /\n               \\ . . .        \\\\                                 _--_/ _/\n                \\              \\\\                              _- _/ _/\n                \\               \\\\                      ___-(O) _/ _/ \n                \\                \\                  __--  __   /_ /      ***********************************\n                \\                 \\\\          ____--__----  /    \\_       I AM A MOTHERFUCKING PTERODACTYL\n                 \\                  \\\\       -------       /   \\_  \\_     HERE TO PTERO-YOU A NEW ASSHOLE\n                  \\                   \\                  //   // \\__ \\_   **********************************\n                   \\                   \\\\              //   //      \\_ \\_ \n                    \\                   \\\\          ///   //          \\__- \n                    \\                -   \\\\/////////    //            \n                    \\            -         \\_         //              \n                    /        -                      //                \n                   /     -                       ///                  \n                  /   -                       //                      \n             __--/                         ///\n  __________/                            // |               \n//-_________      ___                ////  |                \n        ____\\__--/                /////    |                \n   -----______    -/---________////        |                \n     _______/  --/    \\                   |                 \n   /_________-/       \\                   |                 \n  //                  \\                   /                 \n                       \\.                 /                 \n                       \\     .            /                 \n                        \\       .        /                  \n                       \\\\           .    /                  \n                        \\                /                  \n                        \\              __|                  \n                        \\              ==/                  \n                        /              //                   \n                        /          .  //                    \n                        /   .  .    //                      \n                       /.           /                       \n                      /            //                       \n                      /           /\n                     /          //\n                    /         //\n                 --/         /\n                /          //\n            ////         //\n         ///_________////\n```
source theoatmeal.com source view :)
""")