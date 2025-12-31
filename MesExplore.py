# Raw code from Guillaume

import os
import sys
import pandas as pd

if name == "main":
   output_table = '/scratch/dborooghani/data/2025_09_thomason/output_table.csv'
   DATA_PATH_PINC_BIDS = '/scratch/dborooghani/data/2025_09_thomason/PINC'
   sequence_types_out = ["T2haste4prompts", "T2hasteTR1100"]
   anat_folder = "anat"

# retrieve subjects
subjects_i = os.listdir(DATA_PATH_PINC_BIDS)
subjects = list()
for s in subjects_i:
    if os.path.isdir(os.path.join(DATA_PATH_PINC_BIDS, s)):
       subjects.append(s)
print(subjects)
# retrieve sessions and data
rows = list()
for subject in subjects:
    print("________________" + subject + "_________________")
    dir_subject_out = os.path.join(DATA_PATH_PINC_BIDS, subject)
    for sequence_type in sequence_types_out:
        recon_found = "0"
        seg_found = "0"
        ses = "ses-" + sequence_type
        BIDS_ses_folder = os.path.join(DATA_PATH_PINC_BIDS, subject, ses)
        if os.path.exists(BIDS_ses_folder):
            recon_file = os.path.join(dir_subject_out, ses, "anat", subject+"_"+ses+"_rec-nesvor_T2w.nii.gz")
            if os.path.exists(recon_file):
                recon_found = "1"
            seg_file = os.path.join(dir_subject_out, ses, "anat", subject+"_"+ses+"_rec-nesvor_seg-bounti_dseg.nii.gz")
            if os.path.exists(seg_file):
                seg_found = "1"

            rows.append([subject, sequence_type, recon_found, seg_found])
columns = ["subject", "session", "nesvor_recon", "bounti_seg"]
for row in rows:
    print(row)
df = pd.DataFrame(rows, columns=columns)
df.to_csv(output_table, index=False)
