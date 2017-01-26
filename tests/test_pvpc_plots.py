# -*- coding: utf-8 -*-
"""
Test Cases para datos de PVPC

"""
from unittest import TestCase


class TestsPVPCPlots(TestCase):
    """Tests para el almacén local de datos de PVPC."""

    def test_plots_matplotlib(self):
        """Test de plots de datos de PVPC."""
        from esiosdata import PVPC
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from esiosdata.pvpcplot import pvpcplot_ev_scatter, pvpcplot_grid_hora, pvpcplot_tarifas_hora, FIGSIZE, TARIFAS

        pvpc = PVPC(update=True, verbose=True)
        df_pvpc = pvpc.data['data']
        pvpc_mean_daily, pvpc_mean_monthly = pvpc.get_resample_data()

        # PLOTS EV. DIARIA Y MENSUAL:
        pvpcplot_ev_scatter(pvpc_mean_daily, pvpc_mean_monthly, tarifa='VHC', superposic_anual=False)
        pvpcplot_ev_scatter(pvpc_mean_daily, pvpc_mean_monthly, tarifa='GEN')
        pvpcplot_ev_scatter(pvpc_mean_daily, pvpc_mean_monthly, tarifa='NOC')

        fig, ax = plt.subplots(figsize=FIGSIZE)
        for k in TARIFAS:
            pvpcplot_ev_scatter(pvpc_mean_daily, pvpc_mean_monthly, tarifa=k, superposic_anual=False, ax=ax, plot=False)
        plt.show()

        # PLOTS DIARIOS (O DE INTERVALO HORARIO):
        df_day = df_pvpc.loc['2016-02-23']
        pvpcplot_grid_hora(df_day)
        pvpcplot_grid_hora(df_pvpc.loc['2016-02-10':'2016-02-23'])

        pvpcplot_tarifas_hora(df_pvpc.loc['2016-02-10':'2016-02-23'], plot_perdidas=False)
        pvpcplot_tarifas_hora(df_pvpc.loc['2015-02-10':'2015-02-23'], plot_perdidas=True)