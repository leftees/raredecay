# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:49:45 2016

@author: mayou

Contains the different run-modes for the machine-learning algorithms.
"""
import meta_config

#import config as cfg


def run(runmode):
    """select the right runmode from the parameter and run it"""
    #global run_config
    #run_config = 'config'
    _test1()




def _test1():
    meta_config.run_config='test1_cfg'
    import ml_analysis
    import importlib
    cfg = importlib.import_module(meta_config.run_config)

    print "starting physical module test"
    gb_list = []
    original_list = []
    bins_list = []
    ml_ana = ml_analysis.MachineLearningAnalysis()

    for i in range(1):
        print "starting run number ", i+1
        #gb_reweighter = ml_ana.reweight_mc_real(meta_cfg=cfg.reweight_meta_cfg, **cfg.reweight_cfg)
        gb_reweighter = 'gb_reweighter1.pickle'
        gb_weights = ml_ana.reweight_weights(cfg.reweight_cfg.get('reweight_data_mc'), gb_reweighter)
        #bins_reweighter = ml_ana.reweight_mc_real(meta_cfg=cfg.reweight_meta_cfg_bins, **cfg.reweight_cfg_bins)
        bins_reweighter = 'bins_reweighter1.pickle'
        bins_weights = ml_ana.reweight_weights(cfg.reweight_cfg.get('reweight_data_mc'), bins_reweighter)
        #new_weights = ml_ana.reweight_weights(cfg.reweight_cfg.get('reweight_data_mc'), "reweighter1.pickl.pickle")
        gb_list.append( ml_ana.fast_ROC_AUC(cfg.reweight_cfg.get('reweight_data_mc'),
                            cfg.reweight_cfg.get('reweight_data_real'),
                            weight_original =  gb_weights))
        original_list.append( ml_ana.fast_ROC_AUC(cfg.reweight_cfg.get('reweight_data_mc'),
                            cfg.reweight_cfg.get('reweight_data_real')))
        bins_list.append(ml_ana.fast_ROC_AUC(cfg.reweight_cfg.get('reweight_data_mc'),
                            cfg.reweight_cfg.get('reweight_data_real'),
                            weight_original =  bins_weights))
    ml_ana.draw_distributions([cfg.reweight_cfg.get('reweight_data_mc'),
                              cfg.reweight_cfg.get('reweight_data_real')],
                              labels=['mc', 'real'])
    ml_ana.draw_distributions([cfg.reweight_cfg.get('reweight_data_mc'),
                              cfg.reweight_cfg.get('reweight_data_real')],
                              weights=[gb_weights, None],
                              labels=['mc gb_reweighter', 'real'])
    ml_ana.draw_distributions([cfg.reweight_cfg.get('reweight_data_mc'),
                              cfg.reweight_cfg.get('reweight_data_real')],
                              weights=[bins_weights, None],
                              labels=['mc bins_reweighter', 'real'])
    names_list = ['gb', 'original', 'bins']
    for i, lists in enumerate([gb_list, original_list, bins_list]):
        print "ROC AUC mean " + names_list[i] + ": ", (sum(lists)/1), lists


def _test2():
    pass
# temporary:
if __name__ == '__main__':
    run(1)
