#include "RooRealVar.h"
#include "RooDataHist.h"
#include "RooPlot.h"
#include "RooAbsPdf.h"
#include "RooFitResult.h"
#include "RooAddPdf.h"
#include "RooCMSShape.h"
#include "TCanvas.h"

using namespace RooFit;

void TestPlotter() {

    TCanvas *canvas = new TCanvas();
    
    RooRealVar x("x", "x", 60, 120);

    RooRealVar peak("peak", "peak", 90, 60, 120);
    RooRealVar acms("acms", "acms", 50, 20, 200);
    RooRealVar beta("beta", "beta", 0.2, 0.0, 5.0);
    RooRealVar gamma("gamma", "gamma", 0.036, 0.0, 0.2);
    
    //peak.setVal(90);
    //acms.setVal(50);
    //beta.setVal(0.2);
    //gamma.setVal(0.036);

    RooRealVar a1("a1", "a1", 0, -5, 5);
    RooRealVar a2("a2", "a2", -0.000025, -5, 5);
    //RooRealVar a3("a3", "a3", -0.00000025, -5, 5);
    RooRealVar a3("a3", "a3", 0, -5, 5);

    RooRealVar gamma1("gamma", "gamma", 2, 1, 5);
    RooRealVar beta1("beta", "beta", 2, 1, 5);
    RooRealVar mu1("mu", "mu", 3, -5, 5);

    RooCMSShape cmsShape("cmsShape", "CMS Shape PDF", x, acms, beta, gamma, peak);
    RooPolynomial poly("poly","poly PDF",x, RooArgList(a1,a2,a3));
    RooGamma GammaFunction("gamma PDF","gamma PDF",x,gamma1,beta1,mu1);

    RooPlot *frame = x.frame();

    //cmsShape.plotOn(frame,LineColor(kBlue));

    beta.setVal(0.25);

    //cmsShape.plotOn(frame,LineColor(kRed));
    
    //poly.plotOn(frame,LineColor(kRed));
    GammaFunction.plotOn(frame,LineColor(kRed));

    frame->Draw();

    canvas->SaveAs("gamma.png");

    //acms.Print();
    //sigma.Print();

    delete canvas;
    delete frame;
}


