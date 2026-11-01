---
records:
    - id: HSXR0G758Y
      kind: monograph
      title: Schéma de Picard Local
      creators:
        - name: Jean-François Boutot
          role: author
      date: "1978"
      msc:
        - code: 14B15
          from: zbmath_search
        - code: 14-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1978"
          ids:
            doi: 10.1007/bfb0068424
            zbl: "0371.14005"
            zbl_id: "3577362"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1978"
              ids:
                isbn:
                    - "9783540086505"
                    - "9783540359364"
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
          native_id: 10.1007/bfb0068424
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3577362"
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
    - id: HSXWVKPCQV
      kind: preprint
      title: Curvature, diameter and bounded Betti numbers
      creators:
        - name: Zhongmin Shen
          role: author
        - name: Jyh-Yang Wu
          role: author
      date: "2026-10-13"
      msc:
        - code: 53-XX
          from: arxiv
        - code: 55-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.DG
        - system: arxiv
          code: math.AT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-13"
          ids:
            arxiv: "2610.18530"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.18530"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.18530"
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
