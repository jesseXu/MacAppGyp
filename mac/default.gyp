{
  'target_defaults': {
    'include_dirs': [
      '#TARGETNAME#',
    ],
  },
  'targets':[
    {
      'target_name': '#TARGETNAME#',
      'product_name': '#TARGETNAME#',
      'type': 'executable',
      'mac_bundle': 1,
      'include_dirs':[
        '#TARGETNAME#',
      ],
      'sources':[
        '#TARGETNAME#/main.m',
        '#TARGETNAME#/#TARGETNAME#-Prefix.pch',
        '#TARGETNAME#/AppDelegate.h',
        '#TARGETNAME#/AppDelegate.m',
      ],
      'link_settings':{
        'libraries':[
          '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
        ],
      },
      'mac_bundle_resources':[
        '#TARGETNAME#/Base.lproj/MainMenu.xib',
        '#TARGETNAME#/en.lproj/InfoPlist.strings',
      ],
      'xcode_settings':{
        'INFOPLIST_FILE': '#TARGETNAME#/#TARGETNAME#-Info.plist',
        'CLANG_ENABLE_OBJC_ARC': 'YES',
      },
    },
  ],
}
