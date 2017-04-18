//
//  ViewControllerModel.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "ViewControllerModel.h"
#import "POITableViewCellModel.h"

@implementation ViewControllerModel

- (RACSignal *)fetchData {
    return [RACSignal createSignal:^RACDisposable *(id<RACSubscriber> subscriber) {

        NSArray *resultArray = @[[POITableViewCellModel mockData], [POITableViewCellModel mockData], [POITableViewCellModel mockData]];
        NSInteger index = arc4random_uniform(10);
        if (index % 10) {
            [subscriber sendNext:resultArray];
        } else {
            [subscriber sendError:[NSError errorWithDomain:@"傻了吧" code:2 userInfo:nil]];
        }

        return [RACDisposable disposableWithBlock:^{

        }];
    }];
}

@end
