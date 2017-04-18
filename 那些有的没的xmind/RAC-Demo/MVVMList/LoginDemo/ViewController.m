//
//  ViewController.m
//  loginDemo
//
//  Created by XuAzen on 2017/4/18.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "ViewController.h"
#import <ReactiveCocoa.h>
#import "ViewModel.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UITextField *userTextField;
@property (weak, nonatomic) IBOutlet UITextField *pswTextField;
@property (weak, nonatomic) IBOutlet UILabel *outputLabel;
@property (weak, nonatomic) IBOutlet UIButton *clearBtn;

@property (strong, nonatomic) ViewModel *viewModel;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self testSignal1];

    RAC(self.outputLabel, text) = self.viewModel.outputStringSignal;
    RAC(self.userTextField, textColor) = [[self.viewModel.verifyPhoneSignal distinctUntilChanged] map:^id(NSNumber *value) {
        if (value.boolValue) {
            return [UIColor blackColor];
        } else {
            return [UIColor redColor];
        }
    }];
    RAC(self.pswTextField, textColor) = [[self.viewModel.verifyPSWSignal distinctUntilChanged] map:^id(NSNumber *value) {
        if (value.boolValue) {
            return [UIColor brownColor];
        } else {
            return [UIColor yellowColor];
        }
    }];
}

- (void)testSignal1 {
    RACSignal *signal = [RACSignal createSignal:^RACDisposable *(id<RACSubscriber> subscriber) {
        [subscriber sendNext:@"2"];
        [subscriber sendNext:@"5"];
        [subscriber sendNext:@"0"];
        return nil;
    }].replayLazily.replay.replayLast;

    [[RACScheduler schedulerWithPriority:(RACSchedulerPriorityBackground)] schedule:^{
        NSLog(@"fddfdfd");
        [signal subscribeNext:^(NSString *x) {
            NSLog(@"%@", x);
        }];
    }];

    [[RACScheduler schedulerWithPriority:(RACSchedulerPriorityBackground)] schedule:^{
        NSLog(@"qqqqqqq");
        [signal subscribeNext:^(NSString *x) {
            NSLog(@"%@", x);
        }];
    }];
}

- (ViewModel *)viewModel {
    if (!_viewModel) {
        _viewModel = [[ViewModel alloc] init];
    }
    return _viewModel;
}

@end
