//
//  POITableViewCell.h
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "BaseTableViewCell.h"
#import <Masonry.h>


@interface POITableViewCell : BaseTableViewCell

@property(strong, nonatomic)UIImageView *headerImageView;
@property(strong, nonatomic)UILabel *titleLabel;

@end
