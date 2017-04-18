//
//  ViewControllerViewModel.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "ViewControllerViewModel.h"
#import "ViewControllerModel.h"
#import "POITableViewModel.h"
#import "POITableViewCellModel.h"

@implementation ViewControllerViewModel

- (instancetype)init {
    if (self = [super init]) {
        self.dataSignal = [self.fetchDataCommand.executionSignals flattenMap:^RACStream *(RACSignal *signal) {
            return [signal map:^id(NSArray *cellModels) {
                return [[[cellModels rac_sequence] map:^id(POITableViewCellModel *cellModel) {
                    POITableViewModel *viewModel = [[POITableViewModel alloc] initWithModel:cellModel];
                    return viewModel;
                }] array];  //TODO: - 刚才没加array，导致外面拿到的是单个信号...这个array的作用需要好好探究下
            }];
        }];
        self.errorSignal = self.fetchDataCommand.errors;
    }
    return self;
}

- (RACCommand *)fetchDataCommand {
    if (!_fetchDataCommand) {
        _fetchDataCommand = [[RACCommand alloc] initWithSignalBlock:^RACSignal *(id input) {
            ViewControllerModel *model = [[ViewControllerModel alloc] init];
            return model.fetchData;
        }];
    }
    return _fetchDataCommand;
}

@end
