# API Reference

This section contains the auto-generated documentation from the helper functions for GSA of each FMG-FMG and FMM-FMG models (`gsa_api.md`). Tasks raning from loading data and defining storage and loss moduli, to performing the sensitivity analysis and calculating the sensitivity indices and ploting them are executed separately by various functions.

## FMG-FMG Model

::: scripts.GSA.fmg_gsa_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - modulus_func
        - load_data
        - perform_sensitivity_analysis

::: scripts.GSA.fmg_gsa_vis_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - plot_sensitivity_indices
        - read_excel_range
        - plot_Linf_grouped

## FMM-FMG Model

::: scripts.GSA.fmm_gsa_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - modulus_func
        - load_data
        - perform_sensitivity_analysis

::: scripts.GSA.fmm_gsa_vis_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - plot_sensitivity_indices
        - read_excel_range
        - plot_Linf_grouped