import Locometry


locoGui = Locometry.LocoWidget()
nuke.menu( 'Nuke' ).addCommand( 'Locometry/GUI', lambda: locoGui.show())