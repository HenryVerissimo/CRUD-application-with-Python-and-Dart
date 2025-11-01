import 'package:crud_interface/app/ui/controllers/app_menu_bar_controller.dart';
import 'package:crud_interface/app/ui/components/app_menu_bar.dart';
import 'package:crud_interface/app/ui/pages/create_user_page.dart';
import 'package:crud_interface/app/ui/pages/delete_user_page.dart';
import 'package:crud_interface/app/ui/pages/list_users_page.dart';
import 'package:crud_interface/app/ui/pages/update_user_page.dart';
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
          SizedBox(height: 80, child: AppMenuBar(appMenuBarController)),
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

                if (menuOptions["delete user"]) {
                  return DeleteUserPage();
                }

                if (menuOptions["list users"]) {
                  return ListUsersPage();
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
