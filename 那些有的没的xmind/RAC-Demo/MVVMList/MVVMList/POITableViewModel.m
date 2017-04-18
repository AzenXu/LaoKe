//
//  POITableViewModel.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "POITableViewModel.h"

@implementation POITableViewModel

- (instancetype)initWithModel:(POITableViewCellModel *)model {
    if (self = [super init]) {
        RACSignal *signal = [RACSignal return:model];
        self.titleStringSignal = [signal map:^id(POITableViewCellModel *value) {
            return value.title;
        }];
        self.headerImageSignal = [[signal map:^id(POITableViewCellModel *value) {
            NSData *imageData = [NSData dataWithContentsOfURL:value.url];
            return [UIImage imageWithData:imageData];
        }] subscribeOn:[RACScheduler schedulerWithPriority:(RACSchedulerPriorityBackground)]];
    }
    return self;
}

@end
