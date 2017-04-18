//
//  POITableViewCellModel.h
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface POITableViewCellModel : NSObject

@property(nonatomic, copy)NSString *title;
@property(nonatomic, copy)NSURL *url;

+ (POITableViewCellModel *)mockData;

@end
