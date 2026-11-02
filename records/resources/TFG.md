---
records:
    - id: TFG1K8W1TW
      kind: monograph
      title: Lectures in modern analysis and applications II
      creators:
        - name: J. Glimm
          role: author
        - name: L. Gross
          role: author
        - name: Harish-Chandra
          role: author
        - name: R. V. Kadison
          role: author
        - name: D. Ruelle
          role: author
        - name: I. E. Segal
          role: author
        - name: C. T. Taam
          role: editor
      date: "1970"
      msc:
        - code: 00B15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1970"
          ids:
            doi: 10.1007/bfb0100062
            zbl: "0194.30001"
            zbl_id: "3309163"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1970"
              ids:
                isbn:
                    - "9783540049296"
                    - "9783540362982"
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
          native_id: 10.1007/bfb0100062
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3309163"
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
