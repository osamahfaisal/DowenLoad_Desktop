def open_player(self, index):
        if not self.q_threads:
            model_index = self.frame_query.tableView_results.model().mapToSource(index)
            recid = self.recordings[model_index.row()]

            try:
                player = PlayerMainWindow(docid=recid, parent=self)
                player.show()

            except FileNotFoundError:
                QMessageBox.information(self, "QMessageBox.information()",
                                        "Download the selected item.")
        else:
            QMessageBox.information(self, "QMessageBox.information()",
                                    "Player can not be opened until querying "
                                    "finishes") 