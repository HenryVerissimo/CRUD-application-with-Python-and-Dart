import 'package:crud_interface/src/controllers/app_menu_bar_controller.dart';
import 'package:flutter/material.dart';

class AppMenuBar extends StatefulWidget {
  const AppMenuBar({super.key});

  @override
  State<AppMenuBar> createState() => AppMenuBarState();
}

class AppMenuBarState extends State<AppMenuBar> {
  final appMenuBarController = AppMenuBarController();

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: appMenuBarController,
      builder: (context, chield) {
        final Map menuOptions = appMenuBarController.menuOptions;
        final Function(String) selectOption = appMenuBarController.selectOption;

        return Column(
          children: [
            Expanded(
              child: Row(
                spacing: 50,
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  TextButton(
                    child: Text(
                      "CREATE USER",
                      style: TextStyle(
                        color: menuOptions["create user"]
                            ? Color.fromRGBO(255, 255, 255, 1)
                            : Color.fromRGBO(255, 255, 255, 0.5),
                        fontSize: 20,
                        fontFamily: "MonomaniacOne",
                      ),
                    ),
                    onPressed: () {
                      selectOption("create user");
                    },
                  ),
                  TextButton(
                    child: Text(
                      "LIST USERS",
                      style: TextStyle(
                        color: menuOptions["list users"]
                            ? Color.fromRGBO(255, 255, 255, 1)
                            : Color.fromRGBO(255, 255, 255, 0.5),
                        fontSize: 20,
                        fontFamily: "MonomaniacOne",
                      ),
                    ),
                    onPressed: () {
                      selectOption("list users");
                    },
                  ),
                  TextButton(
                    child: Text(
                      "UPDATE USERS",
                      style: TextStyle(
                        color: menuOptions["update user"]
                            ? Color.fromRGBO(255, 255, 255, 1)
                            : Color.fromRGBO(255, 255, 255, 0.5),
                        fontSize: 20,
                        fontFamily: "MonomaniacOne",
                      ),
                    ),
                    onPressed: () {
                      selectOption("update user");
                    },
                  ),
                  TextButton(
                    child: Text(
                      "DELETE USERS",
                      style: TextStyle(
                        color: menuOptions["delete user"]
                            ? Color.fromRGBO(255, 255, 255, 1)
                            : Color.fromRGBO(255, 255, 255, 0.5),
                        fontSize: 20,
                        fontFamily: "MonomaniacOne",
                      ),
                    ),
                    onPressed: () {
                      selectOption("delete user");
                    },
                  ),
                ],
              ),
            ),
            Divider(color: Color.fromRGBO(77, 219, 124, 1)),
          ],
        );
      },
    );
  }
}
