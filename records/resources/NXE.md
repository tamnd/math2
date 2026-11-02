---
records:
    - id: NXEM5G7MWK
      kind: monograph
      title: Optimal Shape Design
      creators:
        - name: Bernhard Kawohl
          role: author
        - name: Olivier Pironneau
          role: author
        - name: Luc Tartar
          role: author
        - name: Jean-Paul Zolésio
          role: author
        - name: Arrigo Cellina
          role: editor
        - name: António Ornelas
          role: editor
      date: "2000"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
        - code: 49-06
          from: zbmath_search
        - code: 65-06
          from: zbmath_search
        - code: 49K20
          from: zbmath_search
        - code: 65K10
          from: zbmath_search
        - code: 65N55
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2000"
          ids:
            doi: 10.1007/bfb0106739
            zbl: "0954.00031"
            zbl_id: "1550775"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2000"
              ids:
                isbn:
                    - "9783540679714"
                    - "9783540444862"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0106739
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "1550775"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
