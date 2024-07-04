import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._fermataPartenza = None
        self._fermataArrivo = None

    def handlePercorso(self, e):
        if self._fermataPartenza is None or self._fermataArrivo is None:
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text("Attenzione, selezionare le due fermate."))
            return
        totTime, path = self._model.bestPath(self._fermataPartenza, self._fermataArrivo)

        if path == []:
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text(f"Percorso non trovato."))
            return

        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Percorso trovato!"))
        self._view.lst_result.controls.append(ft.Text(f"Il cammino più breve fra "
                                                      f"{self._fermataPartenza} e "
                                                      f"{self._fermataArrivo} impiega "
                                                      f"{totTime} minuti"))
        for p in path:
            self._view.lst_result.controls.append(ft.Text(f"{p}"))

        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.lst_result.controls.append(ft.Text(f"il grafo ha {nNodes} nodi"))
        self._view.lst_result.controls.append(ft.Text(f"il grafo ha {nEdges} archi "))
        self._view._btnCalcola.disabled = False
        self._view.update_page()

    def handleCreaGrafoPesato(self, e):
        self._model.buildGraphPesato()
        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        archiPesoMaggiore = self._model.getArchiPesoMaggiore()
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.lst_result.controls.append(ft.Text(f"il grafo ha {nNodes} nodi"))
        self._view.lst_result.controls.append(ft.Text(f"il grafo ha {nEdges} archi"))
        # for a in archiPesoMaggiore:
        #   self._view.lst_result.controls.append(ft.Text(a))
        self._view._btnCalcola.disabled = False
        self._view._btnCalcolaPercorso.disabled = False
        self._view.update_page()

    def handleCercaRaggiungibili(self, e):
        visited = self._model.getBFSNodes(self._fermataPartenza)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Dalla stazione {self._fermataPartenza} posso raggiungere "
                                                      f"{len(visited)} stazioni"))
        for v in visited:
            self._view.lst_result.controls.append(ft.Text(v))
        self._view.update_page()

    def loadFermate(self, dd: ft.Dropdown()):
        fermate = self._model.fermate

        if dd.label == "Stazione di Partenza":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(text=f.nome,
                                                     data=f,
                                                     on_click=self.read_DD_Partenza))
        elif dd.label == "Stazione di Arrivo":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(text=f.nome,
                                                     data=f,
                                                     on_click=self.read_DD_Arrivo))

    def read_DD_Partenza(self, e):
        print("read_DD_Partenza called ")
        if e.control.data is None:
            self._fermataPartenza = None
        else:
            self._fermataPartenza = e.control.data

    def read_DD_Arrivo(self, e):
        print("read_DD_Arrivo called ")
        if e.control.data is None:
            self._fermataArrivo = None
        else:
            self._fermataArrivo = e.control.data
