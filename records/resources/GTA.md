---
records:
    - id: GTA12W02QZ
      kind: monograph
      title: 'Harmonic Analysis Iraklion 1978: Proceedings of a Conference Held at the University of Crete, Iraklion, Greece, July 1978'
      creators:
        - name: Nicholas Petridis
          role: editor
        - name: Stylianos K. Pichorides
          role: editor
        - name: Nicolas Varopoulos
          role: editor
      date: "1980"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 43-06
          from: zbmath_search
        - code: 42-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1980"
          ids:
            doi: 10.1007/bfb0097640
            zbl: "0417.00009"
            zbl_id: "3648648"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1980"
              ids:
                isbn:
                    - "9783540097563"
                    - "9783540386322"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0097640
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3648648"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: GTA6B7SW2V
      kind: preprint
      title: A splitting proximal method in portfolio optimization with entropic value-at-risk
      creators:
        - name: Nail Baloul
          role: author
        - name: Sorin-Mihai Grad
          role: author
        - name: Oleg Wilfer
          role: author
      date: "2026-10-09"
      msc:
        - code: 49-XX
          from: arxiv
        - code: 90-XX
          from: arxiv
        - code: 93-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-09"
          ids:
            arxiv: "2610.14364"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.14364"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.14364"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
