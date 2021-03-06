# Documentation on modules 
=========================================

## data_reader
The **data\_reader** module contains functions to read data from files and operations on these data.

- **read\_training\_data**( file\_list): return a 2-dimensional numpy array contains the information of training data. One row for one peptide. Columns are in the order of amino acid sequence (char list), region type sequence (char list), numbered region type sequence(string list), signal/non\_signal type(int, 1 for singal and 0 for non\_signal) and tm/non\_tm type(int, 1 for tm and 0 for non\_tm). Files and types (i.e. signal/non\_signal, tm/non\_tm) of training data are specified in *file\_list*. 
- **read\_test\_data**(file\_list ): similar to **read\_training\_data**. 
- **get\_rg\_len**( rg\_seq): return the length of n, h and c region of every item in *rg\_seq*.
- **region**( nr\_rg\_seq ): return the corresponding un_numbered region type sequences of the numbered sequences in *nr\_rg\_seq*.
- **number_region**( rg\_seq, n\_max=8, h\_max=18, c\_max = 10): return the corresponding numbered region type sequences of the un_numbered sequences in *rg\_seq*. *n\_max, h\_max, c\_max* are the maximum number of states for each region.
- **rg_replace**(old): replace all 'M', 'o', 'i' with 'O' in *old*def is_sig(rg_seq):
- **is_sig**(rg\_seq): give region sequences *rg\_seq*, return peptide types.

## hmm
The **hmm** module contains functions to build hmm model and make predictions.

- **build_model**(train\_data): return a hmm model as an **hmm\_faster.HMM** instance. *train\_data* should be the same format as output by **data\_reader.read\_training\_data**(file\_list).
- **predict**(model, ob\_seqs, max\_len = 100): given an **hmm\_faster.HMM** instance *model* and a list of observation sequences, return the hidden state sequences. If the length of an observation sequence exceeds *max\_len*, then only the first *max\_len* observations are used for prediction.


