//
//  ViewModel.h
//  MVVMList
//
//  Created by XuAzen on 2017/4/18.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <ReactiveCocoa.h>

@interface ViewModel : NSObject

@property(nonatomic, strong)RACSignal *outputStringSignal;
@property(nonatomic, strong)RACSignal *verifyPhoneSignal;
@property(nonatomic, strong)RACSignal *verifyPSWSignal;

@property(nonatomic, strong)RACChannelTerminal *userTerminal;
@property(nonatomic, strong)RACChannelTerminal *pswTerminal;

@end
