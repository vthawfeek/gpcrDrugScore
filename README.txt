This folder contains files/codes for processing GPCR drug data with respect to their targets, effectors and impacted organs. The codes are written in Python using Jupyter notebooks.


Tissue Expression Score Calculator.ipynb
Required input files
1. Drug:primary/all target list - a csv file with header that contains drug names in the first column and primary/all target names in the second column (drugs with more than one primary target should be in multiple rows) 
2. Target:effector list - a csv file with heafer that contains target names in the first column, receptor names in the second column and union effector count in the third column
3. Target:tissue expression list - a csv file with header that contains target names in the first column and expression values of these targets in different tissues in the subsequent columns (no null values are allowed)
Generated output file
1. Primary/all DES tissue distributed list - a csv file with header that contains drug names in the first column and drug score (calculated using the DES formula described in the text) distributed in different tissues in the subsequent columns


Tissue Expression Distributed Score Calculator.ipynb
Required input files
1. Drug:primary/all target list - a csv file with header that contains drug names in the first column and primary/all target names in the second column (drugs with more than one primary target should be in multiple rows) 
2. Target:effector list - a csv file with heafer that contains target names in the first column, receptor names in the second column and union effector count in the third column
3. Target:tissue expression list - a csv file with header that contains target names in the first column and expression values of these targets in different tissues in the subsequent columns (no null values are allowed)
4. Tissue:organ classification list - a csv file with header that contains tissue names in the first column and matching organ in the second column
5. Net primary/all DES list - a csv file with header that contains drug names in the first column and summed drug score (calculated using the DES formula described in the text) across all tissues in the second column 
Generated output file
1. Primary/all DES organ distributed list - a csv file with header that contains drug names in the first column and drug score percentage (calculated using the DES formula described in the text) distributed in different organs in the subsequent columns


Extended Tissue Expression Score Calculator.ipynb
Required input files
1. Drug:primary/all target list - a csv file with header that contains drug names in the first column and primary/all target names in the second column (drugs with more than one primary target should be in multiple rows) 
2. Target:effector list - a csv file with heafer that contains target names in the first column, receptor names in the second column and union effector count in the third column
3. Target:tissue expression list - a csv file with header that contains target names in the first column and expression values of these targets in different tissues in the subsequent columns (no null values are allowed)
4. Drug:target:dissociation constant list - a csv file with header that contains drug names in the first column, target names in the second column and the dissociation constant (KD) in the third column
5. Drug:dosage list - a csv file with header that contains drug names in the first column and the dosage in the second column
Generated output file
1. Primary/all eDES tissue distributed list - a csv file with header that contains drug names in the first column and drug score (calculated using the eDES formula described in the text) distributed in different tissues in the subsequent columns


Extended Tissue Expression Distributed Score Calculator.ipynb
Required input files
1. Drug:primary/all target list - a csv file with header that contains drug names in the first column and primary/all target names in the second column (drugs with more than one primary target should be in multiple rows) 
2. Target:effector list - a csv file with heafer that contains target names in the first column, receptor names in the second column and union effector count in the third column
3. Target:tissue expression list - a csv file with header that contains target names in the first column and expression values of these targets in different tissues in the subsequent columns (no null values are allowed)
4. Tissue:organ classification list - a csv file with header that contains tissue names in the first column and matching organ in the second column
5. Drug:target:dissociation constant list - a csv file with header that contains drug names in the first column, target names in the second column and the dissociation constant (KD) in the third column
6. Drug:dosage list - a csv file with header that contains drug names in the first column and the dosage in the second column
7. Net primary/all eDES list - a csv file with header that contains drug names in the first column and summed drug score (calculated using the eDES formula described in the text) across all tissues in the second column 
Generated output file
1. Primary/all eDES organ distributed list - a csv file with header that contains drug names in the first column and drug score percentage (calculated using the eDES formula described in the text) distributed in different organs in the subsequent columns
