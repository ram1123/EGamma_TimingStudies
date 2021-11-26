# EGamma_TimingStudies

Timing studies of EGamma paths

```bash
cd /afs/cern.ch/user/r/rasharma/work/EGamma-POG/HLT_tasks/timingStudy
cmsrel CMSSW_11_3_0
cd CMSSW_11_3_0/src
cmsenv
# Download the HLT Configuration
# for one path `HLT_Ele28_WPTight_Gsf_v1`
hltGetConfiguration /dev/CMSSW_11_3_0/GRun --globaltag auto:run3_data_GRun --data --process TIMING --full --offline --max-events 100000 --output none --timing --paths HLTriggerFirstPath,HLTriggerFinalPath,HLT_Ele28_WPTight_Gsf_v1 > hlt_config.py
ssh vocms007
cd /afs/cern.ch/user/r/rasharma/work/EGamma-POG/HLT_tasks/timingStudy/CMSSW_11_3_0/src
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
# Submit the jobs
python3 /data/timing/scripts/timing/submit.py hlt_config.py
# monitor the jobs
python3 /data/timing/scripts/timing/job_manager.py
# Output files can be find here:
cd /data/timing/output/rasharma
```

# Using scripts

1. Get all config files.
   Before running the script check if the `hltGetConfiguration` command is updated one or not. Also check the list of hlt paths and update.
   ```bash
   python GetConfig.py
   ```

2. Submit jobs over all configuration files, generated using previous step.
   ```bash
   ssh vocms007
   cd /afs/cern.ch/user/r/rasharma/work/EGamma-POG/HLT_tasks/timingStudy/CMSSW_12_1_0/src/EGamma_TimingStudies
   cmsenv
   python SubmitMany.py
   ```
   **Note**: The configuration file name format inside the script `SubmitMany.py` should be in consistent with the previous script `GetConfig.py`.

3. Grab results
   ```bash
   python GetResults.py
   ```
   Before running this script one need to update the variable `dirToCheck`. This should be the path where output of previous script is dumped.
   If the path is `/data/timing/jobs/rasharma/CMSSW_12_1_0.20211126_004703`. Then define it like:
   ```python
   dirToCheck = "CMSSW_12_1_0.20211126"
   ```
