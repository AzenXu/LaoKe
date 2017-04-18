//
//  POITableViewCell.m
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import "POITableViewCell.h"
#import "POITableViewModel.h"

@interface POITableViewCell()

@property(strong, nonatomic)POITableViewModel *viewModel;

@end

@implementation POITableViewCell

- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier {
    if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {
        [self setupViews];
    }
    return self;
}

- (void)setupViews {
    [self addSubview:self.headerImageView];
    [self.headerImageView mas_remakeConstraints:^(MASConstraintMaker *make) {
        make.top.equalTo(@10);
        make.bottom.equalTo(@(-10));
        make.left.equalTo(@(10));
        make.width.equalTo(self.headerImageView.mas_height);
    }];

    [self addSubview:self.titleLabel];
    [self.titleLabel mas_remakeConstraints:^(MASConstraintMaker *make) {
        make.left.equalTo(self.headerImageView.mas_right).mas_offset(@10);
        make.centerY.equalTo(self);
        make.right.equalTo(self);
    }];
}

- (void)bindWithViewModel:(POITableViewModel *)viewModel {
    self.viewModel = viewModel;
    RAC(_titleLabel, text) = [viewModel.titleStringSignal takeUntil:self.rac_prepareForReuseSignal];
    RAC(_headerImageView, image) = [viewModel.headerImageSignal takeUntil:self.rac_prepareForReuseSignal];
}

- (UIImageView *)headerImageView {
    if (!_headerImageView) {
        _headerImageView = [[UIImageView alloc] init];
    }
    return _headerImageView;
}

- (UILabel *)titleLabel {
    if (!_titleLabel) {
        _titleLabel = [[UILabel alloc] init];
    }
    return _titleLabel;
}

@end
