//
//  ViewModel.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/18.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "ViewModel.h"

@interface ViewModel()

@property(nonatomic, copy)NSString *psw;
@property(nonatomic, copy)NSString *userName;

@end

@implementation ViewModel

- (instancetype)init {
    if (self = [super init]) {
        self.verifyPSWSignal = [RACObserve(self, psw) map:^id(NSString *psw) {
            return @(YES);
        }];
        self.verifyPhoneSignal = [RACObserve(self, userName) map:^id(NSString *userName) {
            return @(YES);
        }];
        self.outputStringSignal = [RACSignal combineLatest:@[RACObserve(self, psw), RACObserve(self, userName)] reduce:^id (NSString *psw, NSString *phone) {
            return [NSString stringWithFormat:@"用户名:%@, 密码:%@", phone, psw];
        }];
    }
    return self;
}

- (RACChannelTerminal *)userTerminal {
    if (!_userTerminal) {
        _userTerminal = RACChannelTo(self, userName);
    }
    return _userTerminal;
}

- (RACChannelTerminal *)pswTerminal {
    if (!_pswTerminal) {
        _pswTerminal = RACChannelTo(self, psw);
    }
    return _pswTerminal;
}

@end
