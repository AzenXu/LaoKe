//
//  ViewController.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//
//  士兴的Demo是为了讲解MVVM和RAC的几种绑定，所以比较复杂。
//  为了简化数据流，达到更容易入门的效果，这里暂不考虑View复用方面的问题。注意数据的流向。
//  写MVVM代码的时候，依然是缺什么，补什么

#import "ViewController.h"
#import <ReactiveCocoa/ReactiveCocoa.h>
#import "ViewControllerViewModel.h"
#import "POITableViewCell.h"
#import "POITableViewModel.h"

@interface ViewController ()

@property(nonatomic, strong)ViewControllerViewModel *viewModel;
@property(nonatomic, copy)NSArray *cellVMArray; //  这个array的数据从哪来？肯定是有信号过来，把信号拆开得到的，所以一定需要一个装着cellVM的信号 - 提供信号的东东 - viewModel

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self.viewModel.fetchDataCommand execute:nil];
}

- (void)_refreshTableWithArray: (NSArray *)array {
    self.cellVMArray = array;
    [self.tableView reloadData];
}

- (void)_showErrorView: (NSError *)error {
    UIAlertController *errorC = [UIAlertController alertControllerWithTitle:@"啊哦出错了" message:error.domain preferredStyle:(UIAlertControllerStyleAlert)];
    [self presentViewController:errorC animated:YES completion:nil];

}

#pragma mark - lazy
- (ViewControllerViewModel *)viewModel {
    if (!_viewModel) {
        _viewModel = [[ViewControllerViewModel alloc] init];
        [self rac_liftSelector: @selector(_refreshTableWithArray:) withSignals:_viewModel.dataSignal, nil];
        [self rac_liftSelector:@selector(_showErrorView:) withSignals:_viewModel.errorSignal, nil];
    }
    return _viewModel;
}

@end

@implementation ViewController(TableDs)

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return self.cellVMArray.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {

    POITableViewModel *viewModel = self.cellVMArray[indexPath.row];

    POITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"test"];
    if (!cell) {
        cell = [[POITableViewCell alloc] initWithStyle:(UITableViewCellStyleDefault) reuseIdentifier:@"test"];
    }
    [cell bindWithViewModel:viewModel];
    return cell;
}

- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return 100;
}

@end
