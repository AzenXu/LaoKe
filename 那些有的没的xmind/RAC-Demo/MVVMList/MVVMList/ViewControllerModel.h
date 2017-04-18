//
//  ViewControllerModel.h
//  MVVMList
//
//  Created by XuAzen on 2017/4/17.
//  Copyright © 2017年 com.azen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <ReactiveCocoa.h>

@interface ViewControllerModel : NSObject

- (RACSignal *)fetchData;

@end
