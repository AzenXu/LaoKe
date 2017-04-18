//
//  POITableViewCellModel.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "POITableViewCellModel.h"

@implementation POITableViewCellModel

+ (POITableViewCellModel *)mockData {
    POITableViewCellModel *model = [[POITableViewCellModel alloc] init];
    NSInteger index = arc4random_uniform(100);
    model.title = [NSString stringWithFormat:@"测试%ld", (long)index];
    model.url = [NSURL URLWithString:@"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1492443325619&di=cefbaf619fe71ff29c7cd56e804c3f06&imgtype=0&src=http%3A%2F%2Fimg.25pp.com%2Fuploadfile%2Fsoft%2Fimages%2F2015%2F0805%2F20150805013607979.jpg"];
    return model;
}

@end
