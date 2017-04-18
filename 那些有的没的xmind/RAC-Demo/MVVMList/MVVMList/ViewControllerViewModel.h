//
//  ViewControllerViewModel.h
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <ReactiveCocoa.h>

@interface ViewControllerViewModel : NSObject

@property(nonatomic, strong)RACCommand *fetchDataCommand;
@property(nonatomic, strong)RACSignal *dataSignal;
@property(nonatomic, strong)RACSignal *errorSignal;

@end
