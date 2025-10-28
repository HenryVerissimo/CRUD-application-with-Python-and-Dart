import 'package:crud_interface/src/components/app_menu_bar.dart';
import 'package:crud_interface/src/controllers/app_menu_bar_controller.dart';
import 'package:crud_interface/src/pages/create_user_page.dart';
import 'package:crud_interface/src/pages/update_user_page.dart';
import 'package:flutter/material.dart';

class RouterPage extends StatefulWidget {
  const RouterPage({super.key});

  @override
  State<RouterPage> createState() => RouterPageState();
}

class RouterPageState extends State<RouterPage> {
  final appMenuBarController = AppMenuBarController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Expanded(flex: 1, child: AppMenuBar(appMenuBarController)),
          Expanded(
            flex: 11,
            child: ListenableBuilder(
              listenable: appMenuBarController,
              builder: (context, chield) {
                final Map menuOptions = appMenuBarController.menuOptions;

                if (menuOptions["create user"]) {
                  return CreateUserPage();
                }

                if (menuOptions["update user"]) {
                  return UpdateUserPage();
                }

                return Placeholder();
              },
            ),
          ),
        ],
      ),
    );
  }
}
