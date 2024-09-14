#!/usr/bin/env python3
# obsidian-benchmark-vault Source Code
#%%
import os 
import sys
import pathlib
import shutil

import random
num_files = 100
#%%
args = sys.argv

# if len(args)>1:
#     num_files = int(args[1])
# vault_path = "./test_vault"
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
```
--
    -\-                                                     
    \-- \-                                                  
     \  - -\                                                
      \      \\                                             
       \       \                                            
        \       \\                                              
         \        \\                                            
         \          \\                                        
         \           \\\                                      
          \            \\                                                 
           \            \\                                              
           \. .          \\                                  
            \    .       \\                                 
             \      .    \\                                            
              \       .  \\                                 
              \         . \\                                           
              \            <=)                                         
              \            <==)                                         
              \            <=)                                           
               \           .\\                                           _-
               \         .   \\                                        _-//
               \       .     \\                                     _-_/ /
               \ . . .        \\                                 _--_/ _/
                \              \\                              _- _/ _/
                \               \\                      ___-(O) _/ _/ 
                \                \                  __--  __   /_ /      ***********************************
                \                 \\          ____--__----  /    \_       I AM A MOTHERFUCKING PTERODACTYL
                 \                  \\       -------       /   \_  \_     HERE TO PTERO-YOU A NEW ASSHOLE
                  \                   \                  //   // \__ \_   **********************************
                   \                   \\              //   //      \_ \_ 
                    \                   \\          ///   //          \__- 
                    \                -   \\/////////    //            
                    \            -         \_         //              
                    /        -                      //                
                   /     -                       ///                  
                  /   -                       //                      
             __--/                         ///
  __________/                            // |               
//-_________      ___                ////  |                
        ____\__--/                /////    |                
   -----______    -/---________////        |                
     _______/  --/    \                   |                 
   /_________-/       \                   |                 
  //                  \                   /                 
                       \.                 /                 
                       \     .            /                 
                        \       .        /                  
                       \\           .    /                  
                        \                /                  
                        \              __|                  
                        \              ==/                  
                        /              //                   
                        /          .  //                    
                        /   .  .    //                      
                       /.           /                       
                      /            //                       
                      /           /
                     /          //
                    /         //
                 --/         /
                /          //
            ////         //
         ///_________////
```
source theoatmeal.com source view :)
""")