---
records:
    - id: 4TXBCN87MB
      kind: monograph
      title: École d'Été de Probabilités de Saint-Flour XIII — 1983
      creators:
        - name: David J. Aldous
          role: author
        - name: Illdar A. Ibragimov
          role: author
        - name: Jean Jacod
          role: author
        - name: P. L. Hennequin
          role: editor
      date: "1985"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 60-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1985"
          ids:
            doi: 10.1007/bfb0099420
            zbl: "0549.00022"
            zbl_id: "3875188"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1985"
              ids:
                isbn:
                    - "9783540152033"
                    - "9783540393160"
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
          native_id: 10.1007/bfb0099420
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3875188"
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
