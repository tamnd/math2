---
records:
    - id: FSGSVD0XYH
      kind: preprint
      title: Collectivity limits quantum entanglement
      creators:
        - name: Donghoon Kim
          role: author
        - name: Tomotaka Kuwahara
          role: author
      date: "2026-09-28"
      msc:
        - code: 81-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: quant-ph
        - system: arxiv
          code: cond-mat.dis-nn
        - system: arxiv
          code: cond-mat.stat-mech
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.36113"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.36113"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: FSGW2213G0
      kind: monograph
      title: 'Measure Theory: Proceedings of the Conference Held at Oberwolfach, 15–21 June, 1975'
      creators:
        - name: Alexandra Bellow
          role: editor
        - name: Dietrich Kölzow
          role: editor
      date: "1976"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 28-06
          from: zbmath_search
        - code: 46-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi: 10.1007/bfb0081033
            zbl: "0324.00010"
            zbl_id: "3506597"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540078616"
                    - "9783540381075"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0081033
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3506597"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
