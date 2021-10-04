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
