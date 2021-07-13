# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-13
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-13

import os

ListOfPaths = [
        "HLT_Ele28_WPTight_Gsf_v1",
        "HLT_Ele32_WPTight_Gsf_v15",
        "HLT_Ele35_WPTight_Gsf_v9",
        "HLT_DoubleEle25_CaloIdL_MW_v4",
        "HLT_DoubleEle27_CaloIdL_MW_v4",
        "HLT_DoubleEle33_CaloIdL_MW_v17",
        "HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v4",
        "HLT_Photon110EB_TightID_TightIso_v2",
        "HLT_Ele115_CaloIdVT_GsfTrkIdT_v14",
        "HLT_Ele135_CaloIdVT_GsfTrkIdT_v7",
        "HLT_DoublePhoton70_v6",
        "HLT_DoublePhoton85_v14",
        "HLT_Photon200_v13",
        "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v19",
    ]

def main():
    Command = "hltGetConfiguration /dev/CMSSW_11_3_0/GRun --globaltag auto:run3_data_GRun --data --process TIMING --full --offline --max-events 100000 --output none --timing --paths HLTriggerFirstPath,HLTriggerFinalPath%s > hlt_config_13July_%s.py"

    AppendPaths = ""

    for count, paths_ in enumerate(ListOfPaths):
        if count > 1: continue
        print("===")
        command1_ = Command%(","+paths_,count)
        AppendPaths = AppendPaths + ","+paths_
        command2_ = Command%(AppendPaths,"Sum_"+str(count))
        print("Command: {}".format(command1_))
        os.system(command1_)
        print("Command: {}".format(command2_))
        os.system(command2_)




if __name__ == "__main__":
    main()