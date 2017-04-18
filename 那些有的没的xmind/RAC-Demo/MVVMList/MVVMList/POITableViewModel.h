//
//  POITableViewModel.h
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "BaseCellViewModel.h"
#import <ReactiveCocoa.h>
#import "POITableViewCellModel.h"

@interface POITableViewModel : BaseCellViewModel

@property(nonatomic, strong)RACSignal *headerImageSignal;
@property(nonatomic, strong)RACSignal *titleStringSignal;

- (instancetype)initWithModel: (POITableViewCellModel *)model;

@end
