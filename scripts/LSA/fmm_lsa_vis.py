import json
import numpy as np

import sys
import os
sys.path.append(os.path.abspath("../.."))

from scripts.LSA.fmm_lsa_vis_utils import (
    plot_local_sensitivity_indices,
    read_excel_range,
    plot_L1_grouped
)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--E_type', type=str, default=20, help='Type of modulus for which to plot sensitivity indices. E_type = Ep, Epp, or Ecomplex')
    parser.add_argument('--HS', type=int, default=0, help='Index of GnP in GnP_list for which to perform sensitivity analysis. GnP_idx = 0, 1, 2, 3 -> 0%, 0.5%, 1%, and 1.5% GnP')
    args = parser.parse_args()
    
    E_type = args.E_type
    HS = args.HS

    # Load configuration for the specified HSWF content and GnP
    with open(f'../../configs/LSA/{HS}HSWF_FMM_Config.json', 'r') as config_file:
        config = json.load(config_file)

    file_path = config['file_path']
    rows = config['rows']
    cols = config['cols']
    params_list = config['params_list']
    GnP_list = config['GnP_list']

    # Define frequency range for analysis
    w_freq = np.logspace(-8, 2, 500)

    plot_local_sensitivity_indices(E_type, HS, GnP_list, file_path)

    filename = "../../results/LSA/LSA_FMM.xlsx"

    L1_Ep_20HS  = read_excel_range(filename=filename, cell_range="C8:I9")
    L1_Ep_30HS  = read_excel_range(filename=filename, cell_range="C15:I16")
    L1_Ep_40HS  = read_excel_range(filename=filename, cell_range="C22:I23")

    L1_Epp_20HS = read_excel_range(filename=filename, cell_range="M8:S9")
    L1_Epp_30HS = read_excel_range(filename=filename, cell_range="M15:S16")
    L1_Epp_40HS = read_excel_range(filename=filename, cell_range="M22:S23")

    L1_Ecomplex_20HS = read_excel_range(filename=filename, cell_range="W8:AC9")
    L1_Ecomplex_30HS = read_excel_range(filename=filename, cell_range="W15:AC16")
    L1_Ecomplex_40HS = read_excel_range(filename=filename, cell_range="W22:AC23")

    L1_Ep_mean = np.vstack([L1_Ep_20HS[0, :],  L1_Ep_30HS[0, :],  L1_Ep_40HS[0, :]])
    L1_Ep_std = np.vstack([L1_Ep_20HS[1, :],  L1_Ep_30HS[1, :],  L1_Ep_40HS[1, :]])

    L1_Epp_mean = np.vstack([L1_Epp_20HS[0, :], L1_Epp_30HS[0, :], L1_Epp_40HS[0, :]])
    L1_Epp_std = np.vstack([L1_Epp_20HS[1, :], L1_Epp_30HS[1, :], L1_Epp_40HS[1, :]])

    L1_Ecomplex_mean = np.vstack([L1_Ecomplex_20HS[0, :], L1_Ecomplex_30HS[0, :], L1_Ecomplex_40HS[0, :]])
    L1_Ecomplex_std = np.vstack([L1_Ecomplex_20HS[1, :], L1_Ecomplex_30HS[1, :], L1_Ecomplex_40HS[1, :]])

    plot_L1_grouped(
        L1_Ep_mean,
        L1_Ep_std,
        ylabel=r"$||\bar{S}_{E^{\prime}}||_{L_{1}}$",  # E^{\prime} or E^{\prime\prime} or |E^{*}|
        save_path="../../results/LSA/LSA_L1_Ep_FMM"  # Ep or Epp or Ecomplex
    )