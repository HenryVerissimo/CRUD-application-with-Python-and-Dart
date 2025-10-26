import 'package:flutter/material.dart';

class AppMenuBarController extends ChangeNotifier {
  final Map<String, bool> _menuOptions = {
    "create user": true,
    "list users": false,
    "update user": false,
    "delete user": false,
  };

  Map<String, bool> get menuOptions => Map.unmodifiable(_menuOptions);

  void selectOption(String option) {
    _menuOptions[option] = true;

    for (String keyOption in _menuOptions.keys) {
      if (keyOption != option) {
        _menuOptions[keyOption] = false;
      }
    }
    notifyListeners();
  }
}
