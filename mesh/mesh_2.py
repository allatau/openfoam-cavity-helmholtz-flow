#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/dealenx/OpenFOAM/dealenx-5.0/run/Stolb_test/mesh')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("krug", 0.1)
notebook.set("field_length", 10)
notebook.set("field_height", 6)
notebook.set("field_center_x", "field_height/2")
notebook.set("field_center_y", "field_height/2")
notebook.set("left_y1", 1)
notebook.set("left_y2", 2)
notebook.set("right_y1", 3)
notebook.set("right_y2", 4)
notebook.set("field_width", 0.2)
notebook.set("krug", 0.1)
notebook.set("field_length", 10)
notebook.set("field_height", 6)
notebook.set("field_center_x", "field_height/2")
notebook.set("field_center_y", "field_height/2")
notebook.set("left_y1", 1)
notebook.set("left_y2", 2)
notebook.set("right_y1", 3)
notebook.set("right_y2", 4)
notebook.set("field_width", 0.2)
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeBoxDXDYDZ(10, 6, 0.1)
geomObj_2 = geompy.MakeVertex(0, 1, 0)
geomObj_3 = geompy.MakeVertex(0, 2, 0)
Box_1 = geompy.MakeBoxDXDYDZ("field_length", "field_height", "field_width")
Vertex_1 = geompy.MakeVertex(0, "left_y1", 0)
Vertex_2 = geompy.MakeVertex(0, "left_y2", 0)
Vertex_3 = geompy.MakeVertex(0, "left_y1", "field_width")
Vertex_4 = geompy.MakeVertex(0, "left_y2", "field_width")
geomObj_4 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
Edge_1 = geompy.MakeEdge(Vertex_1, Vertex_2)
Edge_2 = geompy.MakeEdge(Vertex_3, Vertex_1)
Edge_3 = geompy.MakeEdge(Vertex_3, Vertex_4)
Edge_4 = geompy.MakeEdge(Vertex_4, Vertex_2)
Face_1 = geompy.MakeFaceWires([Edge_1, Edge_2, Edge_3, Edge_4], 1)
Vertex_5 = geompy.MakeVertex("field_length", "right_y1", 0)
Vertex_6 = geompy.MakeVertex("field_length", "right_y2", 0)
Vertex_7 = geompy.MakeVertex("field_length", "right_y1", "field_width")
Vertex_8 = geompy.MakeVertex("field_length", "right_y2", "field_width")
Edge_5 = geompy.MakeEdge(Vertex_6, Vertex_8)
Edge_6 = geompy.MakeEdge(Vertex_5, Vertex_7)
Edge_7 = geompy.MakeEdge(Vertex_7, Vertex_8)
Edge_8 = geompy.MakeEdge(Vertex_5, Vertex_6)
Face_2 = geompy.MakeFaceWires([Edge_5, Edge_6, Edge_7, Edge_8], 1)
Partition_1 = geompy.MakePartition([Box_1, Face_1, Face_2], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
[geomObj_5,Face_4,geomObj_6,geomObj_7,Face_7,Face_8,geomObj_8,geomObj_9,Face_11,geomObj_10] = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
top = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(top, [55])
in_flow = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(in_flow, [13])
out_flow = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(out_flow, [37])
fixed = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(fixed, [3, 20, 27, 44, 51, 59, 61])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Edge_1, 'Edge_1' )
geompy.addToStudy( Edge_2, 'Edge_2' )
geompy.addToStudy( Edge_3, 'Edge_3' )
geompy.addToStudy( Edge_4, 'Edge_4' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudy( Edge_5, 'Edge_5' )
geompy.addToStudy( Edge_6, 'Edge_6' )
geompy.addToStudy( Edge_7, 'Edge_7' )
geompy.addToStudy( Edge_8, 'Edge_8' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, Face_4, 'Face_4' )
geompy.addToStudyInFather( Partition_1, Face_7, 'Face_7' )
geompy.addToStudyInFather( Partition_1, Face_8, 'Face_8' )
geompy.addToStudyInFather( Partition_1, Face_11, 'Face_11' )
geompy.addToStudyInFather( Partition_1, top, 'top' )
geompy.addToStudyInFather( Partition_1, in_flow, 'in_flow' )
geompy.addToStudyInFather( Partition_1, out_flow, 'out_flow' )
geompy.addToStudyInFather( Partition_1, fixed, 'fixed' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Partition_1)
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(50)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Prism_3D = Mesh_1.Prism()
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=Face_7)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
Projection_1D2D = Mesh_1.Projection1D2D(geom=Face_8)
Source_Face_1 = Projection_1D2D.SourceFace(Face_7,None,None,None,None,None)
NETGEN_2D_Parameters_1.SetMaxSize( 0.3 )
NETGEN_2D_Parameters_1.SetMinSize( 0.1 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 0 )
isDone = Mesh_1.Compute()
top_1 = Mesh_1.GroupOnGeom(top,'top',SMESH.FACE)
in_flow_1 = Mesh_1.GroupOnGeom(in_flow,'in_flow',SMESH.FACE)
out_flow_1 = Mesh_1.GroupOnGeom(out_flow,'out_flow',SMESH.FACE)
fixed_1 = Mesh_1.GroupOnGeom(fixed,'fixed',SMESH.FACE)
try:
  Mesh_1.ExportUNV( r'/home/dealenx/OpenFOAM/dealenx-5.0/run/Stolb_test/mesh/mesh.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
Sub_mesh_1 = NETGEN_1D_2D.GetSubMesh()
Sub_mesh_2 = Projection_1D2D.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Prism_3D.GetAlgorithm(), 'Prism_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Projection_1D2D.GetAlgorithm(), 'Projection_1D2D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(Source_Face_1, 'Source Face_1')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(top_1, 'top')
smesh.SetName(in_flow_1, 'in_flow')
smesh.SetName(out_flow_1, 'out_flow')
smesh.SetName(fixed_1, 'fixed')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
