# API Reference

This section contains the auto-generated documentation from the helper functions for LSA of each FMG-FMG and FMM-FMG models (`lsa_api.md`). Tasks raning from generating the derivative-based normalized local sensitivity indices and loading parameter to performing the monte-carlo simulation for calculating the indices and visualizing them are executed separately by various functions.

## FMG-FMG Model

::: scripts.LSA.fmg_lsa_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - generate_derivatives
        - load_parameter_bounds
        - run_monte_carlo
        - save_statistics_npz

::: scripts.LSA.fmg_lsa_vis_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - plot_local_sensitivity_indices
        - read_excel_range
        - plot_L1_grouped

## FMM-FMG Model

::: scripts.LSA.fmm_lsa_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - generate_derivatives
        - load_parameter_bounds
        - run_monte_carlo
        - save_statistics_npz

::: scripts.LSA.fmm_lsa_vis_utils
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2
      members:
        - plot_local_sensitivity_indices
        - read_excel_range
        - plot_L1_grouped